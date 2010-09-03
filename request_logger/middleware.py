import datetime

from models import RequestLogEntry

class RequestLogger():
    def process_request(self, request):
        time = datetime.datetime.now()
        ip_address = request.META['REMOTE_ADDR']
        url = request.get_full_path()
        request_method = request.META['REQUEST_METHOD']
        user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')
        r = RequestLogEntry(time=time, ip_address=ip_address, url=url, request_method=request_method, user_agent=user_agent)
        r.save()

        return None

