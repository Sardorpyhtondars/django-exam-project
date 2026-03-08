from django.shortcuts import render

def dashboard_view(request):
    return render(request, 'users/dashboard.html')

def login_view(request):
    return render(request, 'users/login.html')
