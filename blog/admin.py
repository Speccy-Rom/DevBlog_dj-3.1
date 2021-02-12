from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published','get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    #fields = ('title', 'category', 'content', 'photo', 'get_photo','is_published', 'views', 'created_at', 'updated_at') # вывод полей на странице записи в админке
    #readonly_fields = ('get_photo','views', 'created_at', 'updated_at') # вывод не изменяемых полей
    save_on_top = True # выводит кнопки управления сверху страницы


    def get_photo(self, obj): #Выводит фото в админ дополнительной колонкой
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '---'
    get_photo.short_description = 'Миниатюра' # переименование надписи в админке

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

