from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import requests
import json

base_api_url = getattr(settings, 'BASE_API_URL', '')

def index(request):
    response = requests.get(f'{base_api_url}/books', auth=('admin', 'admin'))
    if response.status_code == 200:
        return render(request, "books/index.html", {"books": json.loads(response.content)})
    else:
        return HttpResponse('Ошибка при получении данных')

def onebook(request, id):
    response = requests.get(f'{base_api_url}/books/{id}', auth=('admin', 'admin'))
    if response.status_code == 200:
        return render(request, "books/onebook.html", {"book": json.loads(response.content)})
    else:
        return HttpResponse('Ошибка при получении данных')

