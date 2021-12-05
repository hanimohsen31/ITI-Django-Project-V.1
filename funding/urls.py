from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views

app_name = 'funding'
urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.addfunding, name='add'),
    path('list', views.funding_list, name='list'),
    path('confirm_cancel/<int:id>', views.confirm_cancel, name='confirm_cancel'),
    path('cancel/<int:id>', views.cancel_project, name='cancel'),

    path('contacts', views.contacts, name='contacts'),
    path('<int:id>', views.funding_details, name='funding_details'),

    # path('<str:title>', views.filter_title, name='filter_title'),
    # path('<str:category>', views.filter_category, name='filter_category'),
    path('<int:project_id>/reportProject', views.report_project, name="reportProject"),
]
