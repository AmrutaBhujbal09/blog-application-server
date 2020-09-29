from rest_framework import serializers
from .models import BLOG
#here BLOG IS MODEL NAME


class Blogserializer(serializers.ModelSerializer):
    class Meta:
        model = BLOG

        fields = ["id","title","contents","user_id","status","created_at","updated_at"]



class UpdatBlogStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=BLOG
        fields = ["id","status"]
