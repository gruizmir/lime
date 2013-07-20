from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.mainView', name='home'),
    url(r'^/accounts/profile/', 'main.views.userProfile'),
    url(r'^opportunities$', 'main.views.oppsView'),
    url(r'^about$', 'main.views.aboutView'),
    url(r'^blog$', 'main.views.blogView'),
    url(r'^partners$', 'main.views.partnersView'),
    # url(r'^lime/', include('lime.foo.urls')),
    url(r'^accounts/register/', 'main.views.register'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
