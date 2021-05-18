from django.contrib import admin
from .models import Company, UserData

# Register your models here.

@admin.register(Company)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ["id","company_name","company_owner","company_Location","company_city","company_state","company_pincode","company_RegNo"]


@admin.register(UserData)
class UserDataModelAdmin(admin.ModelAdmin):
    list_display = ["id","user","company","name","gender","locality","area","city","zipcode","state","contactNumber","emailId"]

