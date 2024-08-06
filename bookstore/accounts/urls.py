# Path: accounts/urls.py
# Urls for the Accounts app
from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('home', views.home, name='home'),
    path('edit', views.editpage, name='editpage'),
	path('addbook/', views.addbook, name='addbook'),
]