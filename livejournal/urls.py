from django.conf.urls import url, include
from . import views
from .views import PostList, PostDetail

urlpatterns = [
    url(r'^$', PostList.as_view()),
    url(r'^post/(?P<pk>[0-9]+)/$',PostDetail.as_view(), name='post_detail'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
    #url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]