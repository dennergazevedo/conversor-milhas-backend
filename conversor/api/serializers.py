from rest_framework import serializers
from conversor import models

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.User
    fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Brand
    fields = '__all__'
    
class MileSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Mile
    fields = '__all__'
    
class TransactionSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Transaction
    fields = '__all__'