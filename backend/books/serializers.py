from rest_framework import serializers
from .models import Book, Author, BookSale


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_date', 'price', 'is_available')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'email')


class AuthorTotalIncomeSerializer(serializers.ModelSerializer):
    total_income = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ('name', 'total_income')

    def get_total_income(self, obj):
        return obj.total_income
