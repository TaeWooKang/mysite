"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('',views.index ),
    path('<int:id>/',views.detail, name='detail22'),
    path('vote/', views.vote, name='vote'),
    path('<int:number>/data/<str:email>', views.data, name='data'),
    path('input_text',views.input_text, name='input_text'),
    path('add_text',views.add_text, name='add_text'),
    path('result/<int:id>',views.result, name='add_text'),
]
