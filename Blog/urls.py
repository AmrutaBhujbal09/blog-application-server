from django.conf.urls import url
from .views import (CreateBlogAPIView,UpdateBlogStatusAPIView,SelfBlogListView,BlogListView,getBlogDetailsAPIView,searchAPI)

urlpatterns=[
    url('createblog',CreateBlogAPIView.as_view()),
    url('PatchBlog/(?P<pk>.+)',UpdateBlogStatusAPIView.as_view()),
    url('getSelfBlogList',SelfBlogListView.as_view()),
    url('getBlogList',BlogListView.as_view()),
    url('getBlogDetils/(?P<pk>.+)',getBlogDetailsAPIView.as_view()),
    url('search',searchAPI.as_view())
]