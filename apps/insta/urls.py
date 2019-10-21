from django.conf.urls import url, include
from django.contrib import admin
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
	url(r'^$', views.index),
	url(r'^login/$', views.login),
	url(r'^logform/$', views.logform),
	url(r'^register/$', views.register),
	url(r'^registration/$', views.registration),
	url(r'^profile/$', views.profile),
	url(r'^create/$', views.create, name='create'),
	url(r'^create_comment/$', views.create_comment, name='create_comment'),
	url(r'^delete/$', views.delete_message),
	url(r'^logout$', views.logout),
	
]

urlpatterns += staticfiles_urlpatterns()

