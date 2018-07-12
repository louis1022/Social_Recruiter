from django.urls import path
from app import views

urlpatterns = [
    path('message/create/', views.get_message, name='hogehoge'),
    path('message/edit/<int:pk>', views.UpdateMessage.as_view(), name='edit'),
    path('message/delete/<int:pk>', views.DeleteMessage.as_view(), name='delete'),
    path('', views.TopPage.as_view(), name='top_page'),
]
