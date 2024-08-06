from rest_framework import serializers
from .models import Category, Writer, Book, Review, Users
from order.models import Order
from cart.cart import Cart



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ['id', 'name', 'slug', 'bio', 'pic']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'writer', 'category', 'name', 'slug', 'price', 'stock', 'coverpage', 'bookpage', 'created', 'updated', 'totalreview', 'totalrating', 'status', 'description']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'book', 'customer', 'review_star', 'review_text', 'created']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'book', 'quantity', 'created', 'status', 'total']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'name', 'email', 'phone', 'address', 'city', 'province', 'postal_code', 'payment_method', 'account_no', 'transaction_id', 'payable', 'totalbook', 'created', 'updated', 'paid']
