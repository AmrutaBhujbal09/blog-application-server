
from rest_framework.generics import (GenericAPIView,CreateAPIView,ListAPIView,UpdateAPIView)
from .serializers import (Blogserializer,UpdatBlogStatusSerializer)
from rest_framework.response import Response
from .models import BLOG
# Create your views here.

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

