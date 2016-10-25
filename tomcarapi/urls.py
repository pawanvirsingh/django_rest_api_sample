from django.conf.urls import url
from tomcarapi import views

urlpatterns = [
    url(r'^tcars/$', views.tomcarapi_list),
    url(r'^tcars/(?P<pk>[0-9]+)/$', views.tomcarapi_detail),
]