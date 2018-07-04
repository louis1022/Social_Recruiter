from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.TopPage.as_view(), name='top_page'),
    path('dashboard/', views.DashboardPage.as_view(), name='dashboard'),
]
