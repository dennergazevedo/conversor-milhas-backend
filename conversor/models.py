from django.db import models
from uuid import uuid4

class User(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  name = models.CharField(max_length=255)
  email = models.CharField(unique=True, max_length=255)
  password = models.CharField(max_length=255)

class Brand(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  name = models.CharField(unique=True, max_length=255)
  logo = models.CharField(max_length=255)
  value = models.FloatField(default=0)
  tax = models.FloatField(default=0)
    
class Mile(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  userId = models.ForeignKey(User, on_delete=models.CASCADE)
  brandId = models.ForeignKey(Brand, on_delete=models.CASCADE)
  balance = models.FloatField(default=0)
  expiresIn = models.DateField()
    
class Transaction(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  description = models.CharField(max_length=255)
  value = models.FloatField()
  userId = models.ForeignKey(User, on_delete=models.CASCADE)
  type = models.CharField(max_length=50)
  date = models.DateField()