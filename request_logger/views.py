from django.template.context import RequestContext
from django.shortcuts import render_to_response

from request_logger.models import RequestLogEntry

def request_log(request):
    requests = RequestLogEntry.objects.all().order_by('-time')
    return render_to_response('request_log.html',
                              {'requests' : requests, },
                              context_instance=RequestContext(request))

