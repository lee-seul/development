# coding: utf-8

from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
    # 함수형 뷰
    # url(r'^$', views.index, name='index'),
    # url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

    # 클래스형 뷰
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)


