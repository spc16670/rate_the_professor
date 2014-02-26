from django.conf.urls import patterns, url
from rate_the_professor import views

urlpatterns = patterns('',url(r'^$', views.index, name='index')
    , url(r'^professor/(?P<professor_id>\w+)/$', views.professor, name='professor'),)