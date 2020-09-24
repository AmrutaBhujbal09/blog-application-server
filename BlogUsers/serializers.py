from rest_framework import serializers
from .models import User


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","password","username","email","description","linkedin_url","contact_number",
                "Status_Choice"]


    def create(self,validated_data):
        kl=User.objects.create_user(
            first_name=validated_data.pop('first_name'),
            last_name=validated_data.pop('last_name'),
            password=validated_data.pop('password'),
            username=validated_data.pop('username'),
            email=validated_data.pop('email'),
            description=validated_data.pop('description'),
            linkedin_url=validated_data.pop('linkedin_url'),
            contact_number=validated_data.pop('contact_number'),
            Status_Choice=validated_data.pop('Status_Choice')
        )
        return kl