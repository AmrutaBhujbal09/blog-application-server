from django.db import models
from BlogUsers.models import User
from django.utils import timezone
# Create your models here.

class BLOG(models.Model):

    Status_Choice=(
        ('DRAFT','Draft'),
        ('PUBLISHED','Published')
    )




    title = models.CharField(max_length=20,null=False)
    contents = models.TextField(null=False)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=10,null=True,choices=Status_Choice,default='DRAFT')
    created_at = models.TimeField(auto_now=timezone.now)
    updated_at = models.TimeField(auto_now=timezone.now)