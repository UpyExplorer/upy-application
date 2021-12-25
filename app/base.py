# coding=utf-8

"""
Source Base
"""

__all__ = ['BaseUpy']

from django.forms import ModelChoiceField

class BaseUpy():

    def company_id(self):
        return self.request.session['company_data_id']

def get_field_list(model):
    field_list = []
    fields = model._meta.local_fields
    for item in fields:
        if item.is_relation == True:
            field_list.append(item.name + '_id')
        else:
            field_list.append(item.name)

    return field_list

class BaseChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.id
