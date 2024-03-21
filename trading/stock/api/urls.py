from .views import *
from django.urls import path , include



urlpatterns = [    
    path('list', ListStock.as_view(), name='listing-stock'),
    path('userlist', GetStocks.as_view(), name='user-listing-stocks')
]
