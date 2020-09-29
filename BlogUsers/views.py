from rest_framework import status
from rest_framework.generics import(GenericAPIView,CreateAPIView,UpdateAPIView,ListAPIView)
from rest_framework.response import Response
from .serializers import (UserSignUpSerializer,UserLoginSerializer,UpdateUserSerializer)
from .models import User



class UserSignUpAPIView(CreateAPIView):
    serializer_class = UserSignUpSerializer

    def post(self,request, *args, **kwargs):
        print("REQUEST_DATA",request.data)
        serializer=self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            obj=User.objects.get(email=request.data["email"])

            response_data={
                "id":obj.id,
                "first_name":obj.first_name,
                "last_name":obj.last_name,
                "email-address":obj.email
            }

            return Response(response_data)
        else:
            return Response(serializer.errors)


class UserLoginAPIView(GenericAPIView):
     serializer_class=UserLoginSerializer

     def post(self,request,  *args,  **kwargs):
         print("Request data:",request.data)
         serializer = self.get_serializer(data=request.data)

         if serializer.is_valid():
             obj = serializer.Userval

             response_data = {
                 "id": obj.id,
                 "first_name": obj.first_name,
                 "last_name": obj.last_name,
                 "email-address": obj.email
             }

             return Response(response_data)
         else:
             return Response(serializer.errors)


class UpdateUserAPIView(UpdateAPIView):
    serializer_class=UpdateUserSerializer

    def get_queryset(self):
        user_id=self.kwargs['pk']
        return User.objects.filter(id=user_id)

    def patch(self,request,  *args,  **kwargs):
        instance=self.get_object()

        instance.contact_number= request.data["contact_number"]
        instance.description = request.data["description"]
        instance.first_name=request.data["first_name"]
        instance.last_name=request.data["last_name"]
        instance.email=request.data["email"]
        instance.password=request.data["password"]



        serializer = self.get_serializer(instance,data=request.data)
        #given data to serializer for validation...


        if serializer.is_valid(raise_exception=True):
            self.partial_update(serializer)

        return Response(serializer.data,status.HTTP_200_OK)





class GetUserListView (ListAPIView):
    serializer_class = UserSignUpSerializer


    def get_queryset(self):
        return User.objects.filter(is_superuser=False)


    def get(self,request, *args, **kwargs):
        serializer = super().list(request,*args, **kwargs)
        print("SERIALIZER", request.data)
        return Response(serializer.data, status.HTTP_200_OK)