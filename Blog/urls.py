from django.conf.urls import url
from .views import (CreateBlogAPIView,UpdateBlogStatusAPIView,SelfBlogListView,BlogListView,getBlogDetailsAPIView)

urlpatterns=[
    url('createblog',CreateBlogAPIView.as_view()),
    url('PatchBlog/(?P<pk>.+)',UpdateBlogStatusAPIView.as_view()),
    url('getSelfBlogList',SelfBlogListView.as_view()),
    url('getBlogList',BlogListView.as_view()),
    url('getBlogDetils/(?P<pk>.+)',getBlogDetailsAPIView.as_view())
]