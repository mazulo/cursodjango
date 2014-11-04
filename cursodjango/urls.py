from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin


# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns(
    '',
    # url(r'^$', 'cursodjango.views.home', name='home'),
    # url(r'^cursodjango/', include('cursodjango.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^aula3/$', 'aula3.views.index', name='aula3_index'),
    url(r'^aula3/(?P<username>[\w@.]+)/$',
        'aula3.views.detail', name='aula_detail'),
    url(r'^aula4/$', 'aula4.views.index', name='aula4_index'),
    url(r'^aula6/$', 'aula6.views.index', name='aula6_index'),
    url(r'^aula6/add/$', 'aula6.views.add_contato', name='aula6_add_contato'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

urlpatterns += staticfiles_urlpatterns()
