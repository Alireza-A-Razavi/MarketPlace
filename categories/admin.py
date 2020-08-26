from django.contrib import admin
from .models import Category, CategoryVariation, Variation

admin.site.register(Category)
admin.site.register(Variation)
admin.site.register(CategoryVariation)