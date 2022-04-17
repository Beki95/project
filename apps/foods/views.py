from rest_framework.generics import ListAPIView

# Create your views here.
from apps.foods.models import FoodCategory
from apps.foods.serializers import FoodListSerializer


class FoodListAPIView(ListAPIView):
    serializer_class = FoodListSerializer
    queryset = FoodCategory.objects.filter(food__isnull=False, food__is_publish=True) \
        .prefetch_related('food', 'food__additional') \
        .distinct()
