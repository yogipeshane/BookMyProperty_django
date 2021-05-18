from django.shortcuts import render
from .forms import  UserProfileForm , UserRegistrationForm
from django.views import View
from django.contrib import messages
from .models import UserData


# Create your views here.

def home(request):
    return render(request,'core/home.html')

class UserRegistrationView(View):
    def get(self,request):
        form = UserRegistrationForm()
        return render(request, 'core/userRegistration.html',{'form':form})

    def post(self,request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulations ! Registered Successfully.")
            form.save()
        return render(request, 'core/userRegistration.html',{'form':form})

class UserInfoView(View):
    def get(self,request):
        form = UserProfileForm()
        return render(request,'core/user_info.html',{'form':form , 'active': 'btn-warning'})

    def post(self,request):
        form = UserProfileForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            company = form.cleaned_data['company']
            gender = form.cleaned_data['gender']
            locality = form.cleaned_data['locality']
            area = form.cleaned_data['area']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            contactNumber = form.cleaned_data['contactNumber']
            emailId = form.cleaned_data['emailId']

            UserData(user=request.user , company =company ,created_by=request.user,name=name,gender=gender, locality=locality, area=area ,city=city, zipcode=zipcode,
            state=state ,contactNumber=contactNumber,  emailId=emailId ).save()

            messages.success(request, 'Congratulations !! Customer Information updated Successfully.')
        return render(request,'core/user_info.html',{'form': form, 'active': 'btn-warning'})

def UserProfile(request):
    try:
        userData = UserData.objects.get(user= request.user)
        print("userData :", userData)
        return render(request, 'core/user_profile.html', {'userData': userData, 'active': 'btn-warning'})
    except:
        return render(request, 'core/user_profile.html', {'mesg': 'Please enter user Information !', 'active': 'btn-warning'})

