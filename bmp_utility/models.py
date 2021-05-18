from django.db import models
from datetime import date

# Create your models here.
class CommonFields(models.Model):
    created_by = models.CharField(max_length=50)
    modified_by = models.CharField(max_length=50,blank=True)
    created_Date = models.DateField(auto_now_add=True)
    modified_Date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True