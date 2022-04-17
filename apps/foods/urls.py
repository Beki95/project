from django.urls import path

from apps.foods.views import FoodListAPIView

urlpatterns = [
    path('foods/', FoodListAPIView.as_view(), name='foods')
]
