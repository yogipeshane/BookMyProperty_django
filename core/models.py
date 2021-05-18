from django.db import models
from bmp_utility.models import CommonFields
from django.contrib.auth.models import  User

# Create your models here.
STATE_CHOICES = (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
)

GENDER_CHOICES=(
    ('Male','Male'),
    ('Female','Female'),
)


class Company(CommonFields):
   company_name = models.CharField(max_length=50)
   company_owner = models.CharField(max_length=50)
   company_Location = models.CharField(max_length=50)
   company_city = models.CharField(max_length=50)
   company_state = models.CharField(max_length=50, choices=STATE_CHOICES)
   company_pincode = models.IntegerField()
   company_RegNo = models.CharField(max_length=50)

   def __str__(self):
      return self.company_name


class UserData(CommonFields):
   user = models.ForeignKey(User, on_delete=models.CASCADE, )
   company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
   name = models.CharField(max_length=100)
   gender = models.CharField(choices=GENDER_CHOICES, max_length=7, default="M")
   locality = models.CharField(max_length=100)
   area = models.CharField(max_length=100)
   city = models.CharField(max_length=50)
   zipcode = models.IntegerField()
   state = models.CharField(choices=STATE_CHOICES, max_length=50)
   contactNumber = models.IntegerField()
   emailId = models.EmailField()

   def __str__(self):
      return str(self.id)


# class Seller(CommonFields):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,  )
#     sellerName = models.CharField(max_length=100)
#     gender = models.CharField(choices=GENDER_CHOICES, max_length=7, default="M")
#     locality = models.CharField(max_length=100)
#     area = models.CharField(max_length=100)
#     city = models.CharField(max_length=50)
#     zipcode = models.IntegerField()
#     state = models.CharField(choices=STATE_CHOICES, max_length=50)
#     contactNumber = models.IntegerField()
#     emailId = models.EmailField()
#
#     def __str__(self):
#         return str(self.id)
