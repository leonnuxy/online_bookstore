from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from store.forms import AddBookForm
# Import login_required
from django.contrib.auth.decorators import login_required
from store.models import Book, Category, Writer
from order.models import Order, OrderItem
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from store.serializers import BookSerializer
from django.contrib import messages



# Create your views here.

# Views for views.home and views.edit

@login_required
def home(request):
    # Show user information orders placed by user
    orders = Order.objects.filter(customer=request.user)
    context = {
        "orders": orders,
    }
    return render(request, 'accounts/home.html', context)


# Edit user profile
def editpage(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password changed successfully')
            return redirect('store:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, 'accounts/edit.html', context)

def addbook(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            cn = form.clean_name()
            cp = form.clean_price()
            cs = form.clean_stock()
            cd = form.clean_description()
            book = Book(name=cn, price=cp, stock=cs, description=cd, category=Category.objects.get(id=form.cleaned_data['category']), writer=Writer.objects.get(id=form.cleaned_data['writer']))
            book.save()
            messages.success(request, 'Book added successfully')
            return redirect('accounts:home')
    else:
        form = AddBookForm()
    context = {
        "form": form,
    }
    return render(request, 'accounts/addbook.html', context)

