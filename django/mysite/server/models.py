from django.db import models

# Create your models here.
  
class Enquirie(models.Model):
    name=models.CharField(max_length=20,editable=False)
    email=models.CharField(max_length=30,editable=False)
    companyname=models.CharField(max_length=20,editable=False)
    contactnumber=models.IntegerField(editable=False)
    address=models.TextField(editable=False)
    gst=models.CharField(max_length=15,editable=False)
    comments=models.TextField(editable=False)
    status=models.BooleanField(default=False)
   
class Scrap(models.Model):
    name=models.CharField(max_length=20)
    # desc=models.TextField()
    img=models.CharField(max_length=30,default="img")
    current_stock=models.IntegerField()
    Add_Stock=models.IntegerField(default=0)
    current_cost=models.IntegerField()
    
    