from django.conf.urls import url
from .views import (UserSignUpAPIView,UserLoginAPIView,UpdateUserAPIView,GetUserListView)

urlpatterns=[
    url('signup',UserSignUpAPIView.as_view()),
    url('login',UserLoginAPIView.as_view(),name="login"),
    url('patchUser/(?P<pk>.+)',UpdateUserAPIView.as_view()),
    url('userlist',GetUserListView.as_view())
]