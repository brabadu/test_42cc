from django.conf.urls.defaults import *

from request_logger.models import RequestLogEntry


urlpatterns = patterns('',
    url(r'^$',
        'request_logger.views.request_list',
        name='request_log',
       ),

    url(r'^priority/(\d+)/$',
        'request_logger.views.priority_list',
        name='priority_request_log',
       ),
    url(r'^logentry/(\d+)/up$',
        'request_logger.views.priority_change',
        kwargs={
            'up': True,
        },
        name='priority_up_request_log',
       ),
    url(r'^logentry/(\d+)/$',
        'request_logger.views.priority_change',
        kwargs={
            'up': False,
        },
        name='priority_down_request_log',
       ),
)
