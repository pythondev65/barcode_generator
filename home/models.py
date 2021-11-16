from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class signup_data(AbstractUser):
    phonenumber = models.TextField(max_length=10)


class Location(models.Model):
    IIN = models.BigIntegerField()
    State = models.CharField(max_length=30,null=True,blank=True)
    Abbreviation = models.CharField(max_length=30,null=True,blank=True)
    Country = models.CharField(max_length=30,null=True,blank=True)

class barcode(models.Model):
    user = models.ForeignKey(signup_data,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.SET_NULL,null=True,blank=True)
    dlnumber = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    dclass = models.CharField(max_length=100)
    rcode = models.CharField(max_length=100)
    ecode = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    edate = models.CharField(max_length=100)
    idate = models.CharField(max_length=100)
    udate = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    eyeclr = models.CharField(max_length=100)
    hairclr = models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES)
    discriminator = models.CharField(max_length=100)
    connum = models.CharField(max_length=100)
    barcode_img = models.FileField(max_length=100,null=True,blank=True)