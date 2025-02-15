from django.contrib import admin
from django.urls import path, include
from . import views, API_views

urlpatterns = [
    path('', views.chat_view, name="chatAPI"),
    path('apiV1/', API_views.ChatAPIView.as_view(), name='chat-api'),
    path('apiV1/load-data/', views.load_data_api, name="loadData"),
]