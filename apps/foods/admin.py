from django.contrib import admin

# Register your models here.
from apps.foods.models import Food, FoodCategory


@admin.register(Food)
class FoodsAdmin(admin.ModelAdmin):
    ...


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    ...
