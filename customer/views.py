from django.shortcuts import render
from django.views  import View
# Create your views here.

# class customerinfo(View):
#     def customerinfo(self,request, propertyid):
#         return render(request, 'customer/newCustomer.html')

def customerinfo(request,propertyid):
    return render(request,'customer/newCustomer.html')
