from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.views.generic import ListView, DetailView
from blog.models import post

from . import views


urlpatterns = [
    #url(r'^$', views.home, name='home'),
    url('login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url('logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^$', ListView.as_view(queryset=post.objects.all().order_by("-date")[:25], template_name="blog.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=post, template_name='post.html'))
]