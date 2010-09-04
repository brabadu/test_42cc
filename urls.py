from django.conf.urls.defaults import *
from person_contacts.views import contacts
from request_logger.views import request_log

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    url(r'^$',
        view=contacts,
        name='contacts'),
    url(r'^request_log$',
        view=request_log,
        name='request_log')

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
