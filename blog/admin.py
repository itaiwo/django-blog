from django.contrib import admin
from .models import posts, Author

# Register your models here.
admin.site.register(posts)
admin.site.register(Author)