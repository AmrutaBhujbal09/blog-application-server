from django.conf.urls import url
from .views import UserSignUpAPIView

urlpatterns=[
    url('hello',UserSignUpAPIView.as_view())
]