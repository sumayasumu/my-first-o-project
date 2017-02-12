from django.conf.urls import url
from . import views
urlpatterns = [
     url(r'^$', views.index, name='index'),
    url(r'^account/new/$', views.account_new, name='account_new'),
    url(r'^post/list/$', views.post_list, name='post_list'),


    url(r'^deposit/$', views.deposit, name='deposit'),

    url(r'^widraw/$', views.widraw, name='widraw'),
]
