import datetime

from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget

from person_contacts.models import Person


class PersonForm(ModelForm):
    birth_date = SelectDateWidget()

    class Meta:
        model = Person
        fields = [field.name for field in reversed(Person._meta.fields[1:])]
        widgets = {
            'birth_date': SelectDateWidget(years=range(1970,
                                            datetime.datetime.now().year + 1)),
        }
