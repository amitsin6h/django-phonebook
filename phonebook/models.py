from django.db import models

# Create your models here.

class PhoneBook(models.Model):
	name = models.CharField(max_length=250)
	phone = models.CharField(max_length=10)
	email = models.EmailField(max_length=250)
	address = models.CharField(max_length=300)