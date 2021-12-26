# coding=utf-8

"""
Source Base
"""

__all__ = ['BaseViewUpy']

from django.forms import ModelChoiceField


class BaseViewUpy():
    """
    """
    def company_id(self):
        return self.request.session['company_data_id']


class BaseChoiceField(ModelChoiceField):
    """
    """
    def label_from_instance(self, obj):
        return "%s" % obj.id
