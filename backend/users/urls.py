from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView
from django.http import JsonResponse


urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('health', lambda request: JsonResponse({"status": "Server is running"}, status=200), name='health_check')

]