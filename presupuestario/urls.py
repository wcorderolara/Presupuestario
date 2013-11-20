from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from bases.views import login

urlpatterns = patterns('',
	# Examples:
    # url(r'^$', 'presupuestario.views.home', name='home'),
    # url(r'^presupuestario/', include('presupuestario.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login.as_view() , name='login'),
    #url(r'^$', include(bases.urls)),
    
)