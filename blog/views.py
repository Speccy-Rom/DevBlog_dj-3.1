from django.http import HttpResponse
from django.shortcuts import render

from .models import News


def index(request):
    news = News.objects.all()
    contect = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, 'blog/index.html', contect)
