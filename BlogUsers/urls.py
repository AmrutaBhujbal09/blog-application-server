from django.conf.urls import url
from .views import (UserSignUpAPIView,UserLoginAPIView)

urlpatterns=[
    url('hello',UserSignUpAPIView.as_view()),
    url('login',UserLoginAPIView.as_view(),name="login")
]