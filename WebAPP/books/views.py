from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
import requests
import json

def index(request):
    # response = requests.get(reverse(index), auth=('admin', 'admin'))
    response = requests.get('http://localhost:8000/books', auth=('admin', 'admin'))
    if response.status_code == 200:
        return render(request, "books/index.html", {"books": json.loads(response.content)})
    else:
        return HttpResponse('Ошибка при получении данных')

def onebook(request, id):
    # response = requests.get(reverse(onebook, args=[id]), auth=('admin', 'admin'))
    response = requests.get(f'http://localhost:8000/books/{id}', auth=('admin', 'admin'))
    if response.status_code == 200:
        return render(request, "books/onebook.html", {"book": json.loads(response.content)})
    else:
        return HttpResponse('Ошибка при получении данных')

