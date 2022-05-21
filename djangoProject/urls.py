"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a1/', views.view1),
    path('login/', views.login_user),
    path('logout/', views.logout_view),
    path('create/', views.create_user),
    path('check/', views.check_status),
    path('a2/', csrf_exempt(views.SampleClassView.as_view()))
]
