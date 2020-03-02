from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    surname = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=254)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    photo = models.ImageField(upload_to='photos/')