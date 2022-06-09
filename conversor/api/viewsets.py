from rest_framework import viewsets
from conversor.api import serializers
from conversor import models
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.UserSerializer
  queryset = models.User.objects.all()
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['email', 'id']
  
class BrandViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.BrandSerializer
  queryset = models.Brand.objects.all()
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['id', 'name', 'value', 'tax']
  
class MileViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.MileSerializer
  queryset = models.Mile.objects.all()
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['userId', 'brandId', 'balance', 'expiresIn']
  
class TransactionViewset(viewsets.ModelViewSet):
  serializer_class = serializers.TransactionSerializer
  queryset = models.Transaction.objects.all()
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['userId', 'value', 'type', 'date']