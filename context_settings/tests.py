from django.test import TestCase
from django.test import Client

from django.core.urlresolvers import reverse

class SettingsContextTest(TestCase):
    def setUp(self):
        self.client = Client()

    def testcontext(self):
        """
        Test that passes context
        """
        response = self.client.get('/')
        context = response.context['settings']
        self.failUnlessEqual(context is not None, True)

