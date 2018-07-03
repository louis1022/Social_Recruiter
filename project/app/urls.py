from django.urls import path
from app.views import TopPage

app_name='app'
urlpatterns = [
    path('', TopPage.as_view(), name='top_page'),
]
