from django import  forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.utils.translation import gettext, gettext_lazy as _

from .models import UserData


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True , 'class':'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}),
    )

class UserRegistrationForm(UserCreationForm):

    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ("username",'email' ,'password1' ,'password2')
        label = {'email':'Email'},
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ["company","name" , "gender" , "locality" , "area" , "city" , "zipcode" ,"state","contactNumber","emailId"]
        widgets = {
                   'company': forms.Select(attrs={'class': 'form-control'}),
                   'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'gender': forms.Select(attrs={'class': 'form-control'}),
                   'locality': forms.TextInput(attrs={'class': 'form-control'}),
                   'area': forms.TextInput(attrs={'class': 'form-control'}),
                   'city': forms.TextInput(attrs={'class': 'form-control'}),
                   'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
                   'state': forms.Select(attrs={'class': 'form-control'}),
                   'contactNumber': forms.NumberInput(attrs={'class': 'form-control'}),
                   'emailId': forms.EmailInput(attrs={'class': 'form-control'}),

                   }
