from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    GENDER_CHOICES = [('Male','Male'),('Female','Female'),('Other','Other')]


    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=100,choices=GENDER_CHOICES)
    address = models.TextField()
    city = models.CharField(max_length=20,blank=True,null=True)
    contact_no = PhoneNumberField(region='IN')
    adhar_card_no = models.CharField(max_length=30)

    
    