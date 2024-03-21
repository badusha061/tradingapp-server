from django.urls import path , include
from .views import UserViewSet
from rest_framework_simplejwt.views import (
   TokenRefreshView,
)
from .views import * 


urlpatterns = [    
    path('user', UserViewSet.as_view({'post':'create'}),name='user-register'),
    path('token',CustomerTokenObtainPairView.as_view() , name='token_obtain_pair'),
    path('token/refersh/',TokenRefreshView.as_view(), name='token_refersh'),
]
