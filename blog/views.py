from django.shortcuts import render, get_object_or_404, redirect

from .models import News, Category
from .forms import NewsForm


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, 'blog/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    # category = Category.objects.get(pk=category_id)
    category = get_object_or_404(Category, pk=category_id)
    context_category = {
        'news': news,
        'category': category,
    }
    return render(request, 'blog/category.html', context_category)


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'blog/view_news.html', {'news_item': news_item})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST) # форма связана с данными
        if form.is_valid(): # условие прошла ли форма валидацию
            # print(form.cleaned_data)
            news = News.objects.create(**form.cleaned_data) # сохраняем данные введеные через форму не связанной с моделями
            return redirect(news) # редирект на страницу новости
    else:
        form = NewsForm() # форма не связана с данными
    return render(request, 'blog/add_news.html', {'form': form})