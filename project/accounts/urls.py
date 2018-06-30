import django.contrib.auth.views
from django.urls import path,include
from . import views


app_name='accounts'
urlpatterns=[
    path('top/',views.top_page, name="top"),
    path('login/',
        django.contrib.auth.views.login,
        {
            'template_name': 'login.html',
        },
         name='login'),
    path('logout/',
        django.contrib.auth.views.logout,
        {
            'template_name': 'logout.html',
        },
        name='logout'),
]
