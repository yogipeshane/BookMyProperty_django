
from django.urls import path
from property import views

urlpatterns = [
    path('plans', views.planList, name='plans'),
    path('plans/<slug:data>', views.planList, name='plansList'),
    path('aminities/<int:id>', views.Aminities.as_view(), name='aminities'),
    path('property/<int:planid>', views.property.as_view(), name='property')
]