from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from person_contacts.models import Person


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
        person = response.context[-1]['person']
        self.failUnlessEqual(str(person), "Larin B.")


class EditintContactsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_exists(self):
        """
        Test that page exists
        """
        response = self.client.get(reverse('contacts_edit'))
        self.failUnlessEqual(response.status_code, 200)

    def test_view2(self):
        """
        Test that changes were saved correct
        """

        first_name = 'Name'
        last_name = 'Lastname'
        bio = 'Biography'
        telephone = '091 145 67 54'
        email = 'test@example.com'
        twitter = 'twiname'

        response = self.client.post(reverse('contacts_edit'),
                                    {first_name: first_name,
                                     last_name: last_name,
                                     bio: bio,
                                     telephone: telephone,
                                     email: email,
                                     twitter: twitter,
                                    })
        person = Person.objects.get(pk=1)
        self.failUnlessEqual(person.first_name, first_name)
        self.failUnlessEqual(person.last_name, last_name)
        self.failUnlessEqual(person.bio, bio)
        self.failUnlessEqual(person.telephone, telephone)
        self.failUnlessEqual(person.email, email)
        self.failUnlessEqual(person.twitter, twitter)
