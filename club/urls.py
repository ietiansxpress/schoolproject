from django.contrib import admin
from django.urls import path, include
from club import views

#Django admin header customization
admin.site.site_header="Developer Akhil"
admin.site.site_title="Welcome to Akhil Dashboard"
admin.site.index_title="Welcome to this Portal"

urlpatterns = [ 
     path('', views.club, name='club'),
   #  path('base', views.base, name='base'),
     path('home', views.club, name='home'),
     path('resister', views.resister, name='resister'),
     path('gallery', views.gallery, name='gallery'),
     path('ourteam', views.ourteam, name='ourteam'),
   
]

