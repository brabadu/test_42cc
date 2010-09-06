from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response

from person_contacts.models import Person
from person_contacts.forms import PersonForm


def contacts(request):
    p = Person.objects.get(pk=1)
    return render_to_response('contacts.html',
                              {'person': p, },
                              context_instance=RequestContext(request))


def contacts_edit(request):
    if request.method == 'POST':
        p = Person.objects.get(pk=1)
        form = PersonForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return render_to_response('contacts_edit.html',
                              {'form': form, },
                              context_instance=RequestContext(request))
    else:
        form = PersonForm(instance=Person.objects.get(pk=1))
        return render_to_response('contacts_edit.html',
                              {'form': form, },
                              context_instance=RequestContext(request))
