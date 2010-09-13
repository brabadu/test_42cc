from django.test import Client
from django.core.urlresolvers import reverse
from tddspry.django import TestCase

from person_contacts.models import Person
from templatetags.edit_link import edit_link


class EditLinkTagTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_tag_person(self):
        """
        Test that tag returns proper url
        """
        person = Person.objects.get(pk=1)
        self.failUnlessEqual(edit_link(person),
                             '/admin/person_contacts/person/1/')
