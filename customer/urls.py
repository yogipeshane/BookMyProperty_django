
from django.urls import path
from customer import views

urlpatterns = [
    path('newCustomer/<int:propertyid>/', views.customerinfo, name='newCustomer')
]
