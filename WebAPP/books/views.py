from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

def index(request):
    response = requests.get('http://localhost:8000/books/', auth=('admin', 'admin'))
    if response.status_code == 200:
        return render(request, "books/index.html", {"books": json.loads(response.content)})
    else:
        return HttpResponse('Ошибка при получении данных')

