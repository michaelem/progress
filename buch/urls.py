from django.conf.urls.defaults import patterns, include, url    

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'progress.views.home', name='home'),
    url(r'^$', 'progress.buch.views.progress', name = 'progress'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)