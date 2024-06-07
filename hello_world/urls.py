from django.urls import path
from hello_world import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/bitcoin-price/', views.get_bitcoin_price, name='bitcoin-price'),
    path('api/bitcoin-price-last-year/', views.get_bitcoin_price_last_year, name='bitcoin-price-last-year'),
]