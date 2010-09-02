from django.test import TestCase
from django.test import Client

from django.core.urlresolvers import reverse

class ContactsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view1(self):
        """
        Test that view exists and passes context
        """
        response = self.client.get(reverse('contacts'))
        self.failUnlessEqual(response.status_code, 200)

    def test_view2(self):
        """
        Test that passes context
        """
        response = self.client.get(reverse('contacts'))
        self.failUnlessEqual(response.context[-1]['person'], "Larin B.")

