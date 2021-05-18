
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import  LoginForm
from core import views
urlpatterns = [
    path('accounts/login',auth_views.LoginView.as_view(template_name='core/login.html' ,
                                                        authentication_form=LoginForm)  , name="login"),
    path('userregistration/', views.UserRegistrationView.as_view(), name='userregistration'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name="logout"),
    path('userprofile', views.UserProfile, name='userprofile')
]