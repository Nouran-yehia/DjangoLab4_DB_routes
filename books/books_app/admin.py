from django.contrib import admin
from .models import Books
from .models import Author

# Register your models here.
admin.site.register(Books)
admin.site.register(Author)
