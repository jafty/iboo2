from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.event_list, name='event_list'),
	url(r'^(?P<pk>[0-9]+)/$', views.event_detail, name='event_detail'),
	url(r'^(?P<pk>[0-9]+)/enter$', views.enter_event, name='enter_event'),
	url(r'^accounts/login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, name='logout'),
	url(r'^register/$', views.register, name='register'),
	url(r'^new/$', views.event_new, name='event_new'),
]