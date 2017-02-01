from django.conf.urls import url

from . import views

app_name = 'open_src_projects'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<project_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^add_project/$', views.add_project, name='add_project'),
    url(r'^(?P<project_id>[0-9]+)/add_comment/$', views.add_comment, name='add_comment'),
]