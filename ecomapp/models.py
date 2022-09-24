from itertools import product
from msilib.schema import Class
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserModel(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    User_Photo=models.ImageField(null=True,blank=True,upload_to='image/')
    User_Address=models.CharField(max_length=250)
    User_Gender=models.CharField(max_length=10)
    User_Age=models.IntegerField()

class catogoryModel(models.Model):
    Catgory_Name=models.CharField(max_length=250)
    
class PrdctModel(models.Model):
    Catagory=models.ForeignKey(catogoryModel,on_delete=models.CASCADE,null=True)    
    Prdct_Name=models.CharField(max_length=250)
    Prdct_Price=models.IntegerField()

class cartmodel(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(PrdctModel,on_delete=models.CASCADE,null=True)