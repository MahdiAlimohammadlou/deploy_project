from django.urls import path
from .views import welcome_message

app_name = 'welcome'
urlpatterns = [
    path('welcome-message/', welcome_message, name="welcome"),
]
