from django.conf.urls import patterns, include, url
from . import views
from photo import settings

urlpatterns = patterns('',
	url(r'^$', views.main, name='main'),
	url(r'^(\d+)/$', views.album, name='album'),
	url(r'^image/(\d+)/$', views.image, name='image'),
	url(r'^(\d+)/(full|thumbnails|edit)/$', views.album, name='album'),
	url(r'^update/$', views.update, name='update'),
	url(r'^search/$', views.search, name='search'),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
)
