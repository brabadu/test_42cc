from django.conf.urls.defaults import *
from person_contacts.views import contacts, contacts_edit

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    url(r'^$',
        view=contacts,
        name='contacts'),
    url(r'^contacts_edit/$',
        view=contacts_edit,
        name='contacts_edit'),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
