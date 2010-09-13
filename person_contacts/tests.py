import datetime

from django.test import Client
from django.core.urlresolvers import reverse
from tddspry.django import TestCase

from person_contacts.models import Person
from person_contacts.forms import PersonForm


class ContactsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view1(self):
        """
        Test that view exists and passes context
        """
        response = self.client.get(reverse('person_contacts'))
        self.failUnlessEqual(response.status_code, 200)

    def test_view2(self):
        """
        Test that passes context
        """
        response = self.client.get(reverse('person_contacts'))
        person = response.context[-1]['person']
        self.failUnlessEqual(str(person), "Larin B.")


class EditintContactsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_exists(self):
        """
        Test that page exists
        """
        response = self.client.get(reverse('person_contacts_edit'))
        self.failUnlessEqual(response.status_code, 200)

    def test_view2(self):
        """
        Test that changes were saved correct
        """

        first_name = 'Name'
        last_name = 'Lastname'
        birth_date = datetime.date(2000, 10, 1)
        bio = 'Biography'
        telephone = '091 145 67 54'
        email = 'test@example.com'
        twitter = 'twiname'

        response = self.client.post(reverse('person_contacts_edit'),
                                    {'first_name': first_name,
                                     'last_name': last_name,
                                     'birth_date': birth_date,
                                     'bio': bio,
                                     'telephone': telephone,
                                     'email': email,
                                     'twitter': twitter,
                                    },
                                    follow=True)
        person = Person.objects.get(pk=1)
        self.failUnlessEqual(person.first_name, first_name)
        self.failUnlessEqual(person.last_name, last_name)
        self.failUnlessEqual(person.bio, bio)
        self.failUnlessEqual(person.telephone, telephone)
        self.failUnlessEqual(person.email, email)
        self.failUnlessEqual(person.twitter, twitter)
        self.assertRedirects(response, reverse('person_contacts'))

    def test_form_fails(self):
        """
        Test that view finds errors in forms and shows them
        Error is nonvalid email adress
        """

        first_name = 'Name'
        last_name = 'Lastname'
        birth_date = datetime.date(2000, 10, 1)
        bio = 'Biography'
        telephone = '091 145 67 54'
        email = 'test-example.com'
        twitter = 'twiname'

        response = self.client.post(reverse('person_contacts_edit'),
                                    {'first_name': first_name,
                                     'last_name': last_name,
                                     'birth_date': birth_date,
                                     'bio': bio,
                                     'telephone': telephone,
                                     'email': email,
                                     'twitter': twitter,
                                    },
                                    follow=True)
        self.assertContains(response, 'Error filling form')


class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.enable_redirect(True)

    def test_login(self):
        # try to access page that needs authorization
        response = self.client.get(reverse('person_contacts_edit'))
        # make sure that we were redirected to login page
        self.assertRedirects(response,
                             reverse('login_page') + '?next=/contacts_edit/')

        # create a user and log in
        self.user = self.helper('create_user')
        self.login(self.helpers.USERNAME, self.helpers.PASSWORD,
                   url=reverse('person_contacts_edit'))

        self.go200('person_contacts_edit')

        # make sure we are on desired place
        self.logout(url=reverse('person_contacts'))
        # make sure we are on contacts view page
        self.url('person_contacts')

    def test_form_fields_reversed(self):
        model_fields = [field.name for field in Person._meta.fields[1:]]
        model_fields.reverse()
        form_fields = PersonForm().Meta.fields
        self.assert_true(model_fields)
        self.assert_true(form_fields)
        self.assert_equal(model_fields, form_fields)
