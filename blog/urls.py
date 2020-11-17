from django.urls import path
from blog.views import *


urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', get_category)

]