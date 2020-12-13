from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import News, Category
from .forms import NewsForm


class HomeNews(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'blog'

    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Главная страница"
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)  # снимает с будликации запись (со стороны фронтенда)


class NewsByCategory(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'blog'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'],
                                   is_published=True)  # снимает с будликации запись (со стороны фронтенда)




# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, 'blog/index.html', context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     # category = Category.objects.get(pk=category_id)
#     category = get_object_or_404(Category, pk=category_id)
#     context_category = {
#         'news': news,
#         'category': category,
#     }
#     return render(request, 'blog/category.html', context_category)


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'blog/view_news.html', {'news_item': news_item})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)  # форма связана с данными
        if form.is_valid():  # условие прошла ли форма валидацию
            # print(form.cleaned_data)
            # news = News.objects.create(**form.cleaned_data) # сохраняем данные введеные через форму не связанной с моделями
            news = form.save()  # применяем метод save для форм связанных с моделями БД
            return redirect(news)  # редирект на страницу новости
    else:
        form = NewsForm()  # форма не связана с данными
    return render(request, 'blog/add_news.html', {'form': form})
