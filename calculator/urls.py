"""
URL configuration for calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from operations.views import SubtractionView,MultiplicationView,AdditionView,FactorialView,PrimenumberView,BmiView,EmiView,TempartureView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sub/',SubtractionView.as_view()),
    path('multiple/',MultiplicationView.as_view()),
    path('add/',AdditionView.as_view()),
    path('factorial/',FactorialView.as_view()),
    path('prime/',PrimenumberView.as_view()),
    path('bmi/',BmiView.as_view()),
    path('emi/',EmiView.as_view()),
    path("temp/",TempartureView.as_view())
]
