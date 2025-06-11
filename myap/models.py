from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.dispatch import receiver
# import uuid
from .manager import UserManager

class User(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6,null=True,blank=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects=UserManager()

    def name(self):
        return self.first_name+" "+self.last_name
    
    def __str__(self):
        return self.email
    
########crerate product

# class Product(models.Model):
#     product_name = models.CharField()
#     product_price = models.IntegerField()
#     product_details = models.TextField()
#     date_created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-date_created']

#     def __str__self(self):
#         return '{} {}'.format(self.product_name)


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=200)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE , related_name='products')
    product_price = models.IntegerField()
    product_details = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__self(self):
        return '{} {}'.format(self.product_name)
    
