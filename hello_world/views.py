from django.shortcuts import render
from django.http import JsonResponse
import requests
from datetime import datetime, timedelta

def home(request):
    return render(request, 'dashboard/home.html')

def get_bitcoin_price(request):
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    data = response.json()
    try:
        bitcoin_price = data['bpi']['USD']['rate']
    except KeyError:
        return JsonResponse({'error': 'API response structure has changed'}, status=500)
    return JsonResponse({'price': bitcoin_price})

def get_bitcoin_price_last_year(request):
    today = datetime.today()
    last_year = today - timedelta(days=365)
    last_year_str = last_year.strftime('%d-%m-%Y')

    url = f'https://api.coingecko.com/api/v3/coins/bitcoin/history?date={last_year_str}'
    response = requests.get(url)
    data = response.json()
    bitcoin_price_last_year = data['market_data']['current_price']['usd']
    return JsonResponse({'price_last_year': bitcoin_price_last_year})
