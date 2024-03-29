# coding=utf-8

"""
Module Docstring
"""

from django.db import transaction
from django.contrib import messages
from django.contrib.auth import login, authenticate, REDIRECT_FIELD_NAME
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LogoutView as BaseLogoutView, PasswordChangeView as BasePasswordChangeView,
    PasswordResetDoneView as BasePasswordResetDoneView, PasswordResetConfirmView as BasePasswordResetConfirmView,
)
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.utils.crypto import get_random_string
from django.utils.decorators import method_decorator
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import View, FormView
from django.conf import settings

from .utils import (
    send_activation_email, send_reset_password_email, send_forgotten_username_email, send_activation_change_email,
)
from .forms import (
    SignInViaUsernameForm, SignInViaEmailForm, SignInViaEmailOrUsernameForm, SignUpForm,
    RestorePasswordForm, RestorePasswordViaEmailOrUsernameForm, RemindUsernameForm,
    ResendActivationCodeForm, ResendActivationCodeViaEmailForm, ChangeProfileForm, ChangeEmailForm,
)

from modules.account.models import Activation
from modules.company.models import CompanyRelationship
from app.base import BaseUpy
from django.core import management
from app.management.commands import setup_company


class GuestOnlyView(View):
    def dispatch(self, request, *args, **kwargs):
        # Redirect to the index page if the user already authenticated
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)

        return super().dispatch(request, *args, **kwargs)


class LogInView(GuestOnlyView, FormView):
    template_name = 'account/log_in.html'

    def get_context_data(self, **kwargs):
        context = super(LogInView, self).get_context_data(**kwargs)
        context['half_bg'] = 'login-half-bg'

        return context

    @staticmethod
    def get_form_class(**kwargs):
        if settings.DISABLE_USERNAME or settings.LOGIN_VIA_EMAIL:
            return SignInViaEmailForm

        if settings.LOGIN_VIA_EMAIL_OR_USERNAME:
            return SignInViaEmailOrUsernameForm

        return SignInViaUsernameForm

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        request = self.request

        # If the test cookie worked, go ahead and delete it since its no longer needed
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()

        # The default Django's "remember me" lifetime is 2 weeks and can be changed by modifying
        # the SESSION_COOKIE_AGE settings' option.
        if settings.USE_REMEMBER_ME:
            if not form.cleaned_data['remember_me']:
                request.session.set_expiry(0)

        login(request, form.user_cache)

        company_data = CompanyRelationship.objects.filter(user=form.user_cache.id).first()
        request.session['company_data_id'] = company_data.company_data_id

        redirect_to = request.POST.get(REDIRECT_FIELD_NAME, request.GET.get(REDIRECT_FIELD_NAME))
        url_is_safe = url_has_allowed_host_and_scheme(redirect_to, allowed_hosts=request.get_host(), require_https=request.is_secure())

        if url_is_safe:
            return redirect(redirect_to)

        return redirect(settings.LOGIN_REDIRECT_URL)


class SignUpView(BaseUpy, GuestOnlyView, FormView):
    template_name = 'account/sign_up.html'
    form_class = SignUpForm

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        context['half_bg'] = 'register-half-bg'

        return context

    def form_valid(self, form):
        user = form.save(commit=False)

        if settings.DISABLE_USERNAME:
            user.username = get_random_string(10)
        else:
            user.username = form.cleaned_data['username']

        if settings.ENABLE_USER_ACTIVATION:
            user.is_active = False

        try:
            with transaction.atomic():
                user.save()
                management.call_command(setup_company.Command(), user.id)
        except Exception:
            messages.error(
                request=self.request,
                message=_('Error!')
            )
            return redirect('account:sign_up')

        if settings.ENABLE_USER_ACTIVATION:
            code = get_random_string(20)

            Activation(
                code=code,
                user=user
            ).save()

            send_activation_email(self.request, user.email, code)

            messages.success(
                request=self.request,
                message=_('You are signed up. To activate the account, follow the link sent to the mail.')
            )
        else:
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=user.username, password=raw_password)
            login(self.request, user)

            messages.success(
                request=self.request,
                message=_('You are successfully signed up!')
            )

        return redirect('dashboard')


class ActivateView(View):

    @staticmethod
    def get(request, code):
        act = get_object_or_404(Activation, code=code)

        # Activate profile
        user = act.user
        user.is_active = True
        user.save()

        # Remove the activation record
        act.delete()

        messages.success(
            request=request,
            message=_('You have successfully activated your account!')
        )

        return redirect('account:log_in')


class ResendActivationCodeView(GuestOnlyView, FormView):
    template_name = 'account/resend_activation_code.html'

    @staticmethod
    def get_form_class(**kwargs):
        if settings.DISABLE_USERNAME:
            return ResendActivationCodeViaEmailForm

        return ResendActivationCodeForm

    def form_valid(self, form):
        user = form.user_cache

        activation = user.activation_set.first()
        activation.delete()

        code = get_random_string(20)

        Activation(
            code=code,
            user=user
        ).save()

        send_activation_email(self.request, user.email, code)

        messages.success(
            request=self.request,
            message=_('A new activation code has been sent to your email address.')
        )

        return redirect('account:resend_activation_code')


class RestorePasswordView(GuestOnlyView, FormView):
    template_name = 'account/restore_password.html'

    @staticmethod
    def get_form_class(**kwargs):
        if settings.RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME:
            return RestorePasswordViaEmailOrUsernameForm

        return RestorePasswordForm

    def form_valid(self, form):
        user = form.user_cache
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        send_reset_password_email(self.request, user.email, token, uid)

        return redirect('account:restore_password_done')


class ChangeProfileView(LoginRequiredMixin, FormView):
    template_name = 'account/profile/change_profile.html'
    form_class = ChangeProfileForm

    def get_context_data(self, **kwargs):
        context = super(ChangeProfileView, self).get_context_data(**kwargs)
        context['view_name'] = _('Change Profile')
        context['view_path'] = _('Dashboard / My Profile / Change Profile')

        return context

    def get(self, request, *args, **kwargs):
        if not self.request.user.has_perm('global_permissions.app_account_change_profile_view'):
            raise PermissionDenied

        self.object = None
        return super().get(request, *args, **kwargs)

    def get_initial(self):
        user = self.request.user
        initial = super().get_initial()
        initial['first_name'] = user.first_name
        initial['last_name'] = user.last_name
        return initial

    def form_valid(self, form):
        user = self.request.user
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()

        messages.success(
            request=self.request,
            message=_('Profile data has been successfully updated.')
        )

        return redirect('account:change_profile')


class ChangeEmailView(LoginRequiredMixin, FormView):
    template_name = 'account/profile/change_email.html'
    form_class = ChangeEmailForm

    def get_context_data(self, **kwargs):
        context = super(ChangeEmailView, self).get_context_data(**kwargs)
        context['view_name'] = _('Change Email')
        context['view_path'] = _('Dashboard / My Profile / Change Email')

        return context

    def get(self, request, *args, **kwargs):
        if not self.request.user.has_perm('global_permissions.app_account_change_email_view'):
            raise PermissionDenied

        self.object = None
        return super().get(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial['email'] = self.request.user.email
        return initial

    def form_valid(self, form):
        user = self.request.user
        email = form.cleaned_data['email']

        if settings.ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE:
            code = get_random_string(20)

            Activation(
                code=code,
                user=user,
                email=email
            ).save()

            send_activation_change_email(self.request, email, code)

            messages.success(
                request=self.request,
                message=_('To complete the change of email address, click on the link sent to it.')
            )
        else:
            user.email = email
            user.save()

            messages.success(
                request=self.request,
                message=_('Email successfully changed.')
            )

        return redirect('account:change_email')


class ChangeEmailActivateView(View):

    @staticmethod
    def get(request, code):
        act = get_object_or_404(Activation, code=code)

        # Change the email
        user = act.user
        user.email = act.email
        user.save()

        # Remove the activation record
        act.delete()

        messages.success(
            request=request,
            message=_('You have successfully changed your email!')
        )

        return redirect('account:change_email')


class RemindUsernameView(GuestOnlyView, FormView):
    template_name = 'account/remind_username.html'
    form_class = RemindUsernameForm

    def form_valid(self, form):
        user = form.user_cache
        send_forgotten_username_email(user.email, user.username)

        messages.success(
            request=self.request,
            message=_('Your username has been successfully sent to your email.')
        )

        return redirect('account:remind_username')


class ChangePasswordView(BasePasswordChangeView):
    template_name = 'account/profile/change_password.html'

    def get_context_data(self, **kwargs):
        context = super(ChangePasswordView, self).get_context_data(**kwargs)
        context['view_name'] = _('Change Password')
        context['view_path'] = _('Dashboard / My Profile / Change Password')

        return context

    def get(self, request, *args, **kwargs):
        if not self.request.user.has_perm('global_permissions.app_account_change_password_view'):
            raise PermissionDenied

        self.object = None
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        # Change the password
        user = form.save()

        # Re-authentication
        login(self.request, user)

        messages.success(
            request=self.request,
            message=_('Your password was changed.')
        )

        return redirect('account:change_password')


class RestorePasswordConfirmView(BasePasswordResetConfirmView):
    template_name = 'account/restore_password_confirm.html'

    def form_valid(self, form):
        # Change the password
        form.save()

        messages.success(
            request=self.request,
            message=_('Your password has been set. You may go ahead and login now.')
        )

        return redirect('account:log_in')


class RestorePasswordDoneView(BasePasswordResetDoneView):
    template_name = 'account/restore_password_done.html'


class LogOutView(LoginRequiredMixin, BaseLogoutView):
    template_name = 'account/log_out.html'
