from django.conf.urls import url
from .views import (CreateBlogAPIView,UpdateBlogStatusAPIView)

urlpatterns=[
    url('createblog',CreateBlogAPIView.as_view()),
    url('PatchBlog/(?P<pk>.+)',UpdateBlogStatusAPIView.as_view())
]