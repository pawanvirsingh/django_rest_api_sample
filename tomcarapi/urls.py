from django.conf.urls import url
from tomcarapi import views

urlpatterns = [
    url(r'^tcars/$', views.snippet_list),
    url(r'^tcars/(?P<pk>[0-9]+)/$', views.snippet_detail),
]