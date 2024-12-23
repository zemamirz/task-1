from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),  # Админка через префикс
    path('', include('tasks.urls')),  # Все маршруты приложения
    path('accounts/', include('django.contrib.auth.urls')),  # Аутентификация через префикс
]