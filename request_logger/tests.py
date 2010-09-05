import datetime

from django.test import TestCase
from django.test import Client

from request_logger.models import RequestLogEntry


user_agent = 'Unknown'


class RequestLoggerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_equals_fails(self):
        """
        Checks that equality test returns False when time is different
        """
        t1 = datetime.datetime.now()
        r1 = RequestLogEntry(time=t1,
                             ip_address='123',
                             url='/',
                             request_method='get',
                             user_agent=user_agent)
        t2 = datetime.datetime.fromordinal(t1.toordinal() + 10 * 1000)
        r2 = RequestLogEntry(time=t2,
                             ip_address='123',
                             url='/',
                             request_method='get',
                             user_agent=user_agent)
        self.failUnlessEqual(r1.equals(r2), False)

    def test_equals_successes(self):
        """
        Checks that equality test returns True when time is the same
        """
        t = datetime.datetime.now()
        r1 = RequestLogEntry(time=t,
                             ip_address='123',
                             url='/',
                             request_method='get',
                             user_agent=user_agent)
        r2 = RequestLogEntry(time=t,
                             ip_address='123',
                             url='/',
                             request_method='get',
                             user_agent=user_agent)
        self.failUnlessEqual(r1.equals(r2), True)

    def test_database_write(self):
        """
        Test that quantity of log entries increases after every request
        """

        log_len_before = RequestLogEntry.objects.count()
        response = self.client.get('/')
        log_len_new = RequestLogEntry.objects.count()
        self.failUnlessEqual(log_len_new, log_len_before + 1)

    def test_database_request_right(self):
        """
        Test that request that request is written to DB right
        """

        t = datetime.datetime.now()
        response = self.client.get('/')

        log_entry = RequestLogEntry(time=t,
                                    ip_address='127.0.0.1',
                                    url='/',
                                    request_method='GET',
                                    user_agent=user_agent)
        r = RequestLogEntry.objects.all().order_by('-time')[0]
        self.failUnlessEqual(log_entry.equals(r), True)