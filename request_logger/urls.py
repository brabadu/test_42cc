from django.conf.urls.defaults import *

from request_logger.models import RequestLogEntry


urlpatterns = patterns('django.views.generic.list_detail',
    url(r'^$',
        'object_list',
        kwargs={
            'queryset': RequestLogEntry.objects.order_by('time')[:10],
            'template_object_name': 'entries',
        },
        name='request_log',
        ),
)
