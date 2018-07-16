from django.urls import path,include

from accounts import views
from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns=[
    path('',views.user_page, name="top"),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
]
