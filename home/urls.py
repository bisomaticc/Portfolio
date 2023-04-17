from django.contrib import admin
from django.urls import path,include
from home  import views

admin.site.site_header = "Rahul Pareek"
admin.site.site_title = " Developed by Rahul Pareek"
admin.site.index_title = "Portfolio"



urlpatterns = [
    path('',views.portfolio,name='portfolio'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('portfolio/',views.portfolio,name='portfolio'),
   
]
