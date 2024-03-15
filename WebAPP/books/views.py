from django.http import HttpResponse
from django_futures.http_client import HttpClient


def index(request):
    client = HttpClient()
    response = client.get('http://localhost:8000/books/', None)
    if response.status_code == 200:
        return HttpResponse(response.content)
    else:
        return HttpResponse('Ошибка при получении данных')
