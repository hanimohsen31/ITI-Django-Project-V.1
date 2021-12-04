from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views

app_name = 'funding'
urlpatterns = [
    path('', views.funding_list, name='list'),
    path('add', views.addfunding, name='add'),
    path('home', views.home, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('<int:id>', views.funding_details, name='funding_details'),
    # path('<str:title>', views.filter_title, name='filter_title'),
    # path('<str:category>', views.filter_category, name='filter_category'),
]
