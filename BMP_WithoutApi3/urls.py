
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name="home"),
    path('userinfo/', views.UserInfoView.as_view(), name='userinfo'),
    path('core',include("core.urls") ),
    path('property',include("property.urls") ),
    # path('customer',include("customer.urls") ),

]+ static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)
