from rest_framework import status
from rest_framework.generics import (GenericAPIView,CreateAPIView,ListAPIView,UpdateAPIView)
from .serializers import (Blogserializer,UpdatBlogStatusSerializer)
from rest_framework.response import Response
from .models import BLOG
# Create your views here.
from BlogUsers.models import  User
class CreateBlogAPIView(CreateAPIView):
    serializer_class = Blogserializer

    def post(self,request, *args, **kwargs):

        print("REQUEST DATA",request.data)

        serializer = self.get_serializer(data=request.data)
        #passing requsted data to serilizer for validation

        if serializer.is_valid(raise_exception=True):
        #serializer checks requsted data is valid or not using is_valid() method
            serializer.save()
            #save() method save the requested data to the databse
        return Response(serializer.data)




class UpdateBlogStatusAPIView(UpdateAPIView):
    serializer_class = UpdatBlogStatusSerializer


    def get_queryset(self):
        blog_id = self.kwargs['pk']
        return BLOG.objects.filter(id=blog_id)


    def POST(self,request, *args, **kwargs):
        instance=self.get_object()
        instance.status = request.data["status"]

        serializer = self.get_serializer(instance,data=request.data)

        if serializer.is_valid(raise_exception=True):
            self.partial-update(serializer)

        return Response(serializer.data,status.HTTP_200_OK)



class SelfBlogListView(ListAPIView):
    serializer_class = Blogserializer

    def post(self,request, *args, **kargs):
        data = list()
        user_id = request.data["user_id"]
        blog_data = BLOG.objects.filter(status="DRAFT").filter(user_id=user_id)
        #BLOG is class
        serializer = self.get_serializer(blog_data,many=True)

        for Blog in serializer.data:
            get_user =User.objects.filter(id=Blog["user_id"]).values("first_name","last_name","email","description",
                                                                       "linkedin_url","contact_number")

            print("USER DETAILS",get_user)

            data.append({
                "id" : Blog["id"],
                "title" : Blog["title"],
                "contents":Blog["contents"],
                "status": Blog["status"],
                "user_id": Blog["user_id"],
                "first_name":get_user[0]["first_name"],
                "last_name" : get_user[0]["last_name"],
                "email" : get_user[0]["email"],
                "description" : get_user[0]["description"],
                "linkedin_url" : get_user[0]["linkedin_url"],
                "contat_number" : get_user[0]["contact_number"],
                "created_at" : Blog["created_at"],
                "updated_at" : Blog["updated_at"]
            })
        return Response(data,status.HTTP_200_OK)

class BlogListView(ListAPIView):
    serializer_class = Blogserializer

    def get_queryset(self):
        get_status = self.request.data["status"]
        blog_data = BLOG.objects.filter(status=get_status)
        return blog_data

    def post(self,request, *args, **kargs):
        data = list()
        get_status = request.data["status"]
        blog_data = BLOG.objects.filter(status=get_status)
        #BLOG is class
        serializer = self.get_serializer(blog_data,many=True)

        for Blog in serializer.data:
            get_user =User.objects.filter(id=Blog["user_id"]).values("first_name","last_name","email","description",
                                                                       "linkedin_url","contact_number")

            print("USER DETAILS",get_user)

            data.append({
                "id" : Blog["id"],
                "title" : Blog["title"],
                "contents":Blog["contents"],
                "status": Blog["status"],
                "user_id": Blog["user_id"],
                "first_name":get_user[0]["first_name"],
                "last_name" : get_user[0]["last_name"],
                "email" : get_user[0]["email"],
                "description" : get_user[0]["description"],
                "linkedin_url" : get_user[0]["linkedin_url"],
                "contat_number" : get_user[0]["contact_number"],
                "created_at" : Blog["created_at"],
                "updated_at" : Blog["updated_at"]
            })
        return Response(data,status.HTTP_200_OK)


class getBlogDetailsAPIView(ListAPIView):
    serializer_class = Blogserializer

    def get(self, request, *args, **kargs):
        data = list()
        blog_id = self.kwargs["pk"]
        blog_data = BLOG.objects.filter(id=blog_id)
        # BLOG is class
        serializer = self.get_serializer(blog_data, many=True)

        for Blog in serializer.data:
            get_user = User.objects.filter(id=Blog["user_id"]).values("first_name", "last_name", "email", "description",
                                                                      "linkedin_url", "contact_number")

            print("USER DETAILS", get_user)

            data.append({
                "id": Blog["id"],
                "title": Blog["title"],
                "contents": Blog["contents"],
                "status": Blog["status"],
                "user_id": Blog["user_id"],
                "first_name": get_user[0]["first_name"],
                "last_name": get_user[0]["last_name"],
                "email": get_user[0]["email"],
                "description": get_user[0]["description"],
                "linkedin_url": get_user[0]["linkedin_url"],
                "contat_number": get_user[0]["contact_number"],
                "created_at": Blog["created_at"],
                "updated_at": Blog["updated_at"]
            })
        return Response(data, status.HTTP_200_OK)








