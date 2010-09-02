from django.http import HttpResponse
from django.shortcuts import render_to_response

from testapp.models import Person

def contacts(request):
    p = Person.objects.get(pk=1)
    return render_to_response('contacts.html', {'person' : p, })

