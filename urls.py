from django.conf.urls.defaults import *
from django.conf import settings

# another comment to check in-browser edition of file on github
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^', include('person_contacts.urls')),
    (r'^requests/', include('request_logger.urls')),
    url(r'^accounts/login/$',
        view='django.contrib.auth.views.login',
        name='login_page'),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG == True:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT}),
)
