from django.contrib import admin
from .models import Product, Category, Author
from django.contrib.auth.models import Group


admin.site.unregister(Group)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'image_tag', 'createdAt']
    search_fields = ['name', ]
    list_filter = ['name', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'bio']
