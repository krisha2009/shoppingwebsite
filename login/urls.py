from django.contrib import admin
from django.urls import path,include
from login import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login.html',views.login,name='login'),
    path('createacc.html',views.createacc,name='createacc'),
    path('login1.html',views.login1,name='login1')
    

]