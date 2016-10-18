from django.conf.urls import url, include
from . import views
from .views import PostList

urlpatterns = [
    url(r'^$', PostList.as_view()),
    url(r'^post/(?P<pk>[0-9]+)/$',views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]