from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from conversor.api import viewsets

route = routers.DefaultRouter()

route.register('users', viewsets.UserViewSet, basename="Users")
route.register('brands', viewsets.BrandViewSet, basename="Brands")
route.register('miles', viewsets.MileViewSet, basename="Miles")
route.register('transactions', viewsets.TransactionViewset, basename="Transactions")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
