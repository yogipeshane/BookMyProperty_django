from django.db import models
from core.models import STATE_CHOICES
# Create your models here.
from bmp_utility.models import CommonFields

# Create your models here.
from core.models import Company

PLAN_TYPE_CHOICES=(
    ('Layout','Layout'),
)

class Plan(CommonFields):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    plan_Name = models.CharField(max_length=100)
    plan_Type = models.CharField(choices=PLAN_TYPE_CHOICES, max_length=10)
    plan_Number = models.IntegerField()
    plan_Location = models.CharField(max_length=100)
    plan_City = models.CharField(max_length=100)
    plan_Area_In_Acres = models.IntegerField()
    plan_date = models.DateTimeField(auto_now_add=True)
    plan_image = models.ImageField(upload_to='planImages')
    plan_description = models.CharField(max_length=500)
    no_of_plots = models.PositiveIntegerField()

    def __str__(self):
        return self.plan_Name


class Amenities(CommonFields):
    amenity_name = models.CharField(max_length=100)
    amenity_description = models.CharField(max_length=500)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    amenity_image = models.ImageField(upload_to='amenityImages')

    def __str__(self):
        return self.amenity_name

class PropertyType(CommonFields):
    property_type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.property_type_name

PROPERTY_AVAILABILITY_CHOICES=(
    ('Available','Available'),
    ('Hold','Hold'),
    ('Sold','Sold'),
)

class Property(CommonFields):
    planId = models.ForeignKey(Plan, models.DO_NOTHING, related_name='Property_PlanId')
    property_Type = models.ForeignKey(PropertyType, models.DO_NOTHING ,related_name='property_propertyType')
    property_Number = models.IntegerField(default=0)
    total_Area_Of_Property = models.IntegerField()
    property_width = models.PositiveIntegerField()
    property_height = models.PositiveIntegerField()
    property_availability = models.CharField(choices=PROPERTY_AVAILABILITY_CHOICES, max_length=10)
    rate_Of_Plot = models.IntegerField()
    stamp_Duty = models.BooleanField(default=False)
    registry = models.BooleanField(default=False)
    RL = models.BooleanField(default=False)
    FSI = models.BooleanField(default=False)
    NA = models.BooleanField(default=False)



