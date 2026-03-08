from django.shortcuts import render

def category_view(request):
    return render(request, 'store/category.html')

def product_view(request):
    return render(request, 'store/product.html')
