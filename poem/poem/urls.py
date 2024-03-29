from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'poem.views.home', name='home'),
    # url(r'^poem/', include('poem.foo.urls')),
    url(r'^login/$', 'poem.views.usLogin', name='usLogin'), # login
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
   (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
)
urlpatterns += staticfiles_urlpatterns()