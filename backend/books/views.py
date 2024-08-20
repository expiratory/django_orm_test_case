from django.db.models import Count, Sum, F
from django.utils.timezone import now
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer, AuthorTotalIncomeSerializer

class TestTaskViewSet(viewsets.GenericViewSet):
    def get_serializer_class(self, *args, **kwargs):
        if self.action == self.first_task.__name__:
            return BookSerializer
        if self.action == self.second_task.__name__:
            return AuthorSerializer
        if self.action == self.third_task.__name__:
            return AuthorTotalIncomeSerializer

    @extend_schema(
        summary="Получения списка всех книг, опубликованных после 1 января 2023 года, которые доступны для покупки и стоимостью менее 30 тугриков."
    )
    @action(detail=False, methods=['get'])
    def first_task(self, request, *args, **kwargs):
        filtred_books_qs = Book.objects.filter(publication_date__gte='2023-01-01', price__lt=30, is_available=True)
        return Response(self.get_serializer(filtred_books_qs, many=True).data)

    @extend_schema(
        summary="Найти автора с наибольшим количеством опубликованных книг."
    )
    @action(detail=False, methods=['get'])
    def second_task(self, request, *args, **kwargs):
        author_qs = Author.objects.filter(
            book__publication_date__lte=now().date()
        ).prefetch_related(
            'book_set'
        ).annotate(
            books_count=Count('book')
        ).order_by(
            '-books_count'
        ).first()
        return Response(self.get_serializer(author_qs).data)

    @extend_schema(
        summary="Рассчитать общий доход от продаж книг для каждого автора."
    )
    @action(detail=False, methods=['get'])
    def third_task(self, request, *args, **kwargs):
        author_income_qs = Author.objects.filter(
            book__publication_date__lte=now().date(),
            book__booksale__sale_date__lte=now().date()
        ).prefetch_related(
            'book_set', 'book_set__booksale_set'
        ).annotate(
            total_income=Sum(F('book__booksale__quantity') * F('book__price'))
        )
        return Response(self.get_serializer(author_income_qs, many=True).data)


    @extend_schema(
        summary='Получить список названий книг, в которых есть слово "Python".'
    )
    @action(detail=False, methods=['get'])
    def fourth_task(self, request, *args, **kwargs):
        books_titles_with_python_in_title = list(Book.objects.filter(
            title__contains='Python'
        ).values_list(
            'title', flat=True
        ))
        return Response(books_titles_with_python_in_title)
