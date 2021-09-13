import os

from django.core.management import BaseCommand
from django.db import connection

from product.models import Category


class Command(BaseCommand):
    help = 'Import test data'

    def handle(self, *args, **options):
        if Category.objects.count():
            self.stderr.write("DB tables is not empty. Import data canceled.")
            return

        cursor = connection.cursor()

        # импорт данных
        base_path = os.path.join("product", "test_data")
        base_template = 'shop_public_product_{}.sql'
        ordered_entities = (
            'category',
            'product',
            'shop',
            'productstate',
        )

        paths = [os.path.join(base_path, base_template.format(entity)) for entity in ordered_entities]
        for path in paths:
            with open(path) as f:
                cursor.execute(f.read())

        # правка счетчиков
        with open(os.path.join(base_path, "change_seq.sql")) as f:
            cursor.execute(f.read())
