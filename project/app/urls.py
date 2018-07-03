from django.urls import path
from app import views


urlpatterns = [
    path('', views.TopPage.as_view(), name='top_page'),
]
