from django.shortcuts import render

def blog_view(request):
    return render(request, 'blog/blog.html')

def blog_listing(request):
    return render(request, 'blog/blog_listing.html')

def single_view(request):
    return render(request, 'blog/single_view.html')
