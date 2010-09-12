import datetime

from django.test import TestCase
from django.test import Client

from database_logger.models import DatabaseChangeLogEntry


class DatabaseChangeLoggerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_database_write(self):
        """
        Test that quantity of log entries increases after every request
        """

        log_len_before = DatabaseChangeLogEntry.objects.count()
        # Making request to a page creates database entry for model
        # RequestLogEntry therefore generates signal that handler must catch
        response = self.client.get('/')

        log_len_new = DatabaseChangeLogEntry.objects.count()
        self.failUnlessEqual(log_len_new, log_len_before + 1)
