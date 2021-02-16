from django.urls import path
from .views import registration_view

app_name = 'api_account'
urlpatterns = [
	path('register/', registration_view, name='register_api'),
]