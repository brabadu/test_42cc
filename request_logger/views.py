from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.list_detail import object_list

from request_logger.models import RequestLogEntry


def priority_list(request, priority):
    queryset = RequestLogEntry.objects.filter(priority=priority)
    queryset = queryset.order_by('time')[:10]
    return object_list(request, queryset=queryset,
                                template_object_name='entries',
                                extra_context={'priority': priority},
                      )


def priority_change(request, request_log_enry_id, up):
    log_entry = RequestLogEntry.objects.get(pk=request_log_enry_id)
    if up:
        log_entry.priority_up()
    else:
        log_entry.priority_down()
    return HttpResponseRedirect(reverse('request_log'))
