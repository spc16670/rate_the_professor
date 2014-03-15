from django.conf.urls import patterns, url
from rate_the_professor import views

urlpatterns = patterns('',url(r'^$', views.index, name='index')
    ,url(r'^professor/(?P<professor_id>\w+)/$', views.professor, name='professor')
    ,url(r'^register/$', views.register, name='register')
    ,url(r'^login/$', views.user_login, name='login')
    ,url(r'^logout/$', views.user_logout, name='logout')
    ,url(r'^user/$', views.user, name='user')
    ,url(r'^suggest_professor/$', views.suggest_professor, name='suggest_professor')
    ,url(r'^suggestion/$', views.suggestion, name='suggestion')
    ,url(r'^ranking/$', views.ranking, name='ranking')
    )