import datetime

from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget

from person_contacts.models import Person


class PersonForm(ModelForm):
    birth_date = SelectDateWidget()

    class Meta:
        model = Person
        widgets = {
            'birth_date': SelectDateWidget(years=range(1970,
                                            datetime.datetime.now().year + 1)),
        }
