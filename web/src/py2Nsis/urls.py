from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^py2Nsis/', include('py2Nsis.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^index/', "py2Nsis.views.index"),
    (r'^try_it/', "py2Nsis.views.try_it"),
    (r'^contact/', "py2Nsis.views.contact"),
    
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/ubugtu/Aptana Studio Workspace/py2Nsis/src/Templates', 'show_indexes': True}),
)
