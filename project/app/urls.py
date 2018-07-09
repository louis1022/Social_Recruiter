from django.urls import path
from app import views


urlpatterns = [
    path('create/', views.CreateMessage.as_view()),
    path('', views.TopPage.as_view(), name='top_page'),
]
