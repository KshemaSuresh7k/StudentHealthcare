from django.db import models

# Create your models here.

class addteacher(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    department=models.CharField(max_length=200,null=True)
    username=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)

class addstudent(models.Model):
    name=models.CharField(max_length=200,null=True)
    sid=models.IntegerField(null=True)
    email=models.CharField(max_length=200,null=True)
    batch=models.CharField(max_length=200,null=True)
    department=models.CharField(max_length=200,null=True)
    username=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)


class addhealth(models.Model):
    name=models.CharField(max_length=200,null=True)
    height=models.IntegerField(null=True)
    weight=models.IntegerField(null=True)
    bloodgroup=models.CharField(max_length=200,null=True)
    drinkingwater=models.CharField(max_length=200,null=True)
    regularperiods=models.CharField(max_length=200,null=True)
    mentalissues=models.CharField(max_length=200,null=True)
    sid=models.IntegerField(null=True)
    department=models.CharField(max_length=200,null=True)


class crud(models.Model):
    image = models.ImageField(null=True,blank=True,upload_to ="images/")


