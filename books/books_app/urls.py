from django.urls import path
from .views import show_all, one_book, author_books

urlpatterns = [
    path('showbooks',show_all),
    path('book/<id>', one_book, name='book'),
    path('author/<id>', author_books, name='author')
]
