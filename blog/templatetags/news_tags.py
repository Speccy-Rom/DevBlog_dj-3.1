from django import template
from django.db.models import Count
from blog.models import Category

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('blog/list_categories.html')
def show_categories():
    categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    # categories = Category.objects.all()
    return {"categories": categories}
