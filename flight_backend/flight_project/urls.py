from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel route (e.g., /admin/)
    path('admin/', admin.site.urls),

    # API routes from the flights app, accessible via /api/
    path('api/', include('flights.urls')),
]
