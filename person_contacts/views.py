from django.http import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import render_to_response

from person_contacts.models import Person


def contacts(request):
    p = Person.objects.get(pk=1)
    return render_to_response('contacts.html',
                              {'person': p, },
                              context_instance=RequestContext(request))
