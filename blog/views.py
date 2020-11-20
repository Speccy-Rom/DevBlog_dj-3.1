from django.http import HttpResponse
from django.shortcuts import render

from .models import News, Category


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, 'blog/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context_category = {
        'news': news,
        'category': category,
    }
    return render(request, 'blog/category.html', context_category)
