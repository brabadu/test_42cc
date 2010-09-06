from django.forms import ModelForm

from person_contacts.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
