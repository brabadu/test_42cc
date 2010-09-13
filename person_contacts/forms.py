import datetime

from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget

from person_contacts.models import Person
from person_contacts.widgets import JQueryDatePickerWidget


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = [field.name for field in reversed(Person._meta.fields[1:])]
        widgets = {
            'birth_date': JQueryDatePickerWidget(),
        }
