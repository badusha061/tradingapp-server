from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from user_auth.api import views
router = DefaultRouter()




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user_auth.api.urls')),
    path('api/', include('stock.api.urls')),
]
