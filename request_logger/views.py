from django.views.generic.list_detail import object_list

from request_logger.models import RequestLogEntry


def priority_list(request, priority):
    queryset = RequestLogEntry.objects.filter(priority=priority)
    queryset = queryset.order_by('time')[:10]
    return object_list(request, queryset=queryset,
                                template_object_name='entries',
                                extra_context={'priority': priority},
                      )
