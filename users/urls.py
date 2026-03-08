from django.urls import path
from users.views import login_view, dashboard_view

app_name = 'users'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
]