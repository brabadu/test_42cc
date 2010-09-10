from django import forms
from django.db import models
from django.template.loader import render_to_string
from django.forms.widgets import DateInput
from django.utils.safestring import mark_safe


class JQueryDatePickerWidget(DateInput):
    def __init__(self, attrs={}):
        attrs['class'] = 'datepicker'
        super(JQueryDatePickerWidget, self).__init__(attrs)

    class Media:
        css = {
            'all': ('/static/css/ui-lightness/jquery-ui-1.8.4.custom.css',),
        }
        js = (
            "/static/js/jquery-1.4.2.min.js",
            "/static/js/jquery-ui-1.8.4.custom.min.js",
            "/static/js/jquery-datepicker.js",
            )
