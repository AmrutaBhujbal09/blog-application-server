from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):

    Status_Choice=(
        ('ACTIVE','Active'),
        ('INACTIVE','Inactive')
    )



    email=models.EmailField('email_address',unique=True)
    contact_number=models.TextField(max_length=10,null=True)
    description=models.TextField(max_length=60,null=True,blank=False)
    linkedin_url=models.URLField(null=True,blank=False)
    Status_Choice=models.CharField(max_length=10,null=True,blank=False,choices=Status_Choice,default='Active')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

