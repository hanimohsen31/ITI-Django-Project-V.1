from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views

app_name = 'funding'
urlpatterns = [
    path('', views.funding_list),
    path('<int:id>', views.funding_details, name='funding_details'),
]
