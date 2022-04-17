import faker
from django.core.management import BaseCommand

from apps.foods.models import FoodCategory


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def get_word(self, lang, nb: int = 5) -> str:
        words = faker.Faker(lang).words(nb=nb)
        word = ' '.join(words)
        return word

    def handle(self, *args, **options):
        count = options.get('count', 5)
        categories = []
        for i in range(count):
            category = FoodCategory(
                name_ru=self.get_word('ru_RU', nb=10),
                name_en=self.get_word('en_US', nb=10),
                name_ch=self.get_word('zh_CN', nb=10),
                order_id=faker.Faker().pyint()
            )
            categories.append(category)
        FoodCategory.objects.bulk_create(categories)
        self.stdout.write(self.style.SUCCESS('Успешно создано %d обьектов' % count))
