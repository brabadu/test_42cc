from django.conf.urls.defaults import *

from person_contacts.views import contacts, contacts_edit


urlpatterns = patterns('',
    url(r'^$',
        view=contacts,
        name='person_contacts'),
    url(r'^contacts_edit/$',
        view=contacts_edit,
        name='person_contacts_edit'),
)
