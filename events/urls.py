from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.event_list, name='event_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.event_detail, name='event_detail'),
]