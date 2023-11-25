"""ocrs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from home.views import homepage,loginpage,signuppage,contact,about,report
from accounts.views import report_crime

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('templates/login.html/',loginpage),
    path('templates/signup.html/',signuppage),
    path('templates/contact.html/',contact),
    path('templates/about.html/',about),
    path('templates/report.html/',report),
    path('reportcrime/',report_crime)
]

