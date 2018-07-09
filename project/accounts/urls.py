from django.urls import path,include

from accounts import views
from django.contrib.auth.views


app_name='accounts'

urlpatterns=[
    path('top/',views.top_page, name="top"),
    path('login/', django.contrib.auth.views.login, name='login'),
    path('logout/', django.contrib.auth.views.logout, name='logout'),
]
