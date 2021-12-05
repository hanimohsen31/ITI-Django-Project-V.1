from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views
from . import api


app_name = 'user'
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('activate/<str:uid>/<str:token>', views.Activate.as_view(), name='activate'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('profile/delete', views.delete, name='delete_profile'),
    path('warn', views.warn, name='warn'),
    path('login/v', api.login_V.as_view(), name='login_v'),
]
