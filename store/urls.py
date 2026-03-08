from django.urls import path
from store.views import product_view, category_view

app_name = 'store'

urlpatterns = [
    path('category/', category_view, name='category'),
    path('product/', product_view, name='product'),
]