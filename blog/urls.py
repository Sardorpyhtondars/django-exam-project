from django.urls import path
from blog.views import blog_view, blog_listing, single_view

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='blog'),
    path('<single/', single_view, name='single'),
    path('listing/', blog_listing, name='listing'),

]