import random

import faker
from django.core.management import BaseCommand

from apps.foods.models import FoodCategory, Food


class Command(BaseCommand):

    def add_arguments(self, parser) -> None:
        parser.add_argument('count', type=int)

    def get_word(self, lang, nb: int = 5) -> str:
        words = faker.Faker(lang).words(nb=nb)
        word = ' '.join(words)
        return word

    def get_categoryes(self) -> list[FoodCategory, ...]:
        categories = FoodCategory.objects.all()
        if not categories:
            raise Exception('Пожалуйста создайте категории по команде fake_category int: необязательно')
        return categories

    def handle(self, *args, **options):
        count = options.get('count', 10)
        foods = []
        categories = self.get_categoryes()
        for i in range(count):
            food = Food(
                category=random.choice(categories),
                is_vegan=faker.Faker().pybool(),
                is_special=faker.Faker().pybool(),
                code=faker.Faker().pyint(),
                internal_code=faker.Faker().pyint(),
                name_ru=self.get_word('ru_RU'),
                description_ru=self.get_word('ru_RU', nb=10),
                description_en=self.get_word('en_US', nb=10),
                description_ch=self.get_word('zh_CN', nb=10),
                cost=faker.Faker().pyint(),
                is_publish=faker.Faker().pybool(),
            )
            foods.append(food)
        Food.objects.bulk_create(foods)
        self.stdout.write(self.style.SUCCESS('Успешно создано %d обьектов' % count))
