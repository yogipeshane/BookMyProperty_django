from django.contrib import admin
from .models import  Plan, Amenities, PropertyType, Property


# Register your models here.


@admin.register(Plan)
class planAdmin(admin.ModelAdmin):
    list_display = ["id", "plan_Name", "plan_Type", "plan_Number", "plan_Location", "plan_City",
                    "plan_Area_In_Acres", "plan_date", "plan_image", "no_of_plots",
                    "created_by", "modified_by", "created_Date", "modified_Date", "is_active"]

@admin.register(Amenities)
class AmenitiesAdmin(admin.ModelAdmin):
    list_display = ["amenity_name" , "amenity_description" , "plan" , "amenity_image",
                    "created_by", "modified_by", "created_Date","modified_Date","is_active"]

@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ["id","property_type_name","created_by", "modified_by", "created_Date",
                    "modified_Date","is_active"]

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ["id","planId","property_Type","property_Number","total_Area_Of_Property","property_width",
                  "property_height","property_availability","rate_Of_Plot","stamp_Duty","registry","RL","FSI",
                  "NA","created_by", "modified_by", "created_Date","modified_Date","is_active"]
