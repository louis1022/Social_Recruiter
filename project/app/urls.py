from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.DashboardPage.as_view(), name='dashboard'),
    path('user/', views.userProfilePage.as_view(), name='user'),
    path('tables/', views.tablesPage.as_view(), name='tables'),
]
