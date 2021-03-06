import datetime

from tddspry.django import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

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
                             user_agent=user_agent,
                             priority=0,
                            )
        t2 = datetime.datetime.fromordinal(t1.toordinal() + 10 * 1000)
        r2 = RequestLogEntry(time=t2,
                             ip_address='123',
                             url='/',
                             request_method='get',
                             user_agent=user_agent,
                             priority=0,
                            )
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
                             user_agent=user_agent,
                             priority=1,
                            )
        r2 = RequestLogEntry(time=t,
                             ip_address='123',
                             url='/',
                             request_method='get',
                             user_agent=user_agent,
                             priority=1,
                            )
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
                                    user_agent=user_agent,
                                    priority=1,
                                   )
        r = RequestLogEntry.objects.all().order_by('-time')[0]
        self.failUnlessEqual(log_entry.equals(r), True)

    def test_first_requests(self):
        """
        Tests that page exists that lists 10 requests from database
        """

        self.go200(reverse('request_log'))
        self.find('/admin/request_logger/requestlogentry/')

    def test_digit_param(self):
        """
        Tests that page is loaded properly
        if parameter for request is in digits
        """
        for i in xrange(20):
            self.go200(reverse('priority_request_log', args=[i]))
            self.find('Priority: %d' % i)

    def test_nondigit_param(self):
        """
        Tests that response is 404
        if parameter for request is in non-digits
        """
        client = Client()
        response = client.get('/requests/abc')
        self.assert_equals(response.status_code, 404)

    def test_priority_change(self):
        """
        Tests that objects's method of model RequestLogEntry
        changes it's priority
        """
        self.go('/')
        log_entry = RequestLogEntry.objects.all()[0]
        priority_old = log_entry.priority

        log_entry.priority_up()
        priority_old += 1
        self.eq_(log_entry.priority, priority_old)

        log_entry.priority_down()
        priority_old -= 1
        self.eq_(log_entry.priority, priority_old)
