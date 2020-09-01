from django.contrib import admin
from .models import Category, CategoryVariation, Variation, MainCategory

admin.site.register(Category)
admin.site.register(MainCategory)
admin.site.register(Variation)
admin.site.register(CategoryVariation)