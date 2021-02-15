from django.urls import path
from .views import (api_detail_view, api_update_view, api_delete_view, api_create_view)

app_name = 'api_post'
urlpatterns = [
	path('<slug>/', api_detail_view, name='api_detail'),
	path('<slug>/update/', api_update_view, name='api_update'),
	path('<slug>/delete/', api_delete_view, name='api_delete'),
	path('create', api_create_view, name='api_create'),
]