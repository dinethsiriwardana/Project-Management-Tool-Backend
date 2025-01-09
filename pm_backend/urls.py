# pm_backend/urls.py (main project URLs)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('projects.urls')),  # This connects to your app's URLs
    path('api/', include('users.urls')),  # This connects to your app's URLs
]