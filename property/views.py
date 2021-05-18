from django.shortcuts import render
from django.views import View
from .models import Plan , Amenities, Property

# Create your views here.
def planList(request , data = None):
    if data == None:
        plans = Plan.objects.all()
    if data == 'Mauli' or data == "Mahalaxmi":
        plans = Plan.objects.filter(company__company_name =data)
    if plans :
        return render(request,'property/plans.html',{'plans':plans})
    else:
        print("In else")
        return render(request, 'property/plans.html', {'mesg': 'Plans will coming soon ! '})

class Aminities(View):
    def get(self, request, id):
        aminities = Amenities.objects.filter(plan=id)
        if aminities:
            return render(request, 'property/aminities.html',{'aminities':aminities})
        else:
            return render(request, 'property/aminities.html',{'mesg': 'Amenities will coming soon ! '})
class property(View):
    def get(self,request, planid):
        if planid:
            propertyList = Property.objects.filter(planId = planid)
            if propertyList:
                return render(request, 'property/property.html',{'propertyList':propertyList })
            else:
                return render(request, 'property/property.html',{'mesg':' Plots are not inserted , It is in progress. Please wait !'})




