from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag
def edit_link(obj):
    app_label = obj._meta.app_label
    model_name = obj._meta.module_name
    return reverse('admin:%s_%s_change' % (app_label, model_name),
                   args=(obj.id,))
