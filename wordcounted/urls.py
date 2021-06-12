
from django.urls import path
from . import views

#if someone clicks on the website a url will be sent and which willtake the user to a page(url)
# create apath were the url will take the user to VIEW the site.
#  creat a html file for the requested page.

urlpatterns = [
    path('', views.homepage, name='home'),
    path('count/', views.count, name='count'),
     path('about/', views.about, name='about'),
    
  
    
]
