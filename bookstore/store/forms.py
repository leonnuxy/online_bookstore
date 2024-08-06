from unicodedata import category
from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Review, Category, Writer

class RegistrationForm(UserCreationForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'username',
            'password1',
            'password2'
        ]
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class ReviewForm(forms.ModelForm):
    review_star = forms.IntegerField(widget=forms.HiddenInput(), initial=1)
    review_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write Your Review'}))

    class Meta:
        model = Review
        fields = [
            'review_star',
            'review_text'
        ]
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


class AddBookForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    category = forms.ChoiceField(choices=[(c.id, c.name) for c in Category.objects.all()], required=True)
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    stock = forms.IntegerField(required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write Your Description'}), required=True)
    coverpage = forms.ImageField(required=True)
    bookpage = forms.ImageField(required=True)
    writer = forms.ChoiceField(choices=[(c.id, c.name) for c in Writer.objects.all()], required=True)
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if Book.objects.filter(name=name).exists():
            raise forms.ValidationError('This book is already in the database.')
        return name

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError('Price must be greater than 0.')
        return price

    def clean_stock(self):
        stock = self.cleaned_data['stock']
        if stock < 0:
            raise forms.ValidationError('Stock must be greater than 0.')
        return stock

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) > 500:
            raise forms.ValidationError('Description must be less than 500 characters.')
        return description



    class Meta:
        model = Book
        fields = [
            'name',
            'slug',
            'price',
            'stock',
            'description',
            'coverpage',
            'bookpage',
            'writer_id',
            'category_id'
        ]
    def __init__(self, *args, **kwargs):
        super(AddBookForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

        

