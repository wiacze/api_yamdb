import csv

from django.apps import apps
from django.core.management.base import BaseCommand

from reviews.models import Category


class Command(BaseCommand):
    help = 'Import CSV data to a Django model'

    def add_arguments(self, parser):
        parser.add_argument(
            'app_name',
            type=str,
            help='Name of the Django app containing the model.'
        )
        parser.add_argument(
            'model_name',
            type=str,
            help='Name of the Django model.'
        )
        parser.add_argument(
            'csv_file',
            type=str,
            help='Path to the CSV file.'
        )

    def handle(self, *args, **options):
        app_name = options['app_name']
        model_name = options['model_name']
        csv_file = f'././static/data/{options["csv_file"]}'

        try:
            model = apps.get_model(app_label=app_name, model_name=model_name)
        except LookupError:
            return f'Model "{model_name}" not found in app "{app_name}".'

        with open(csv_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if model.__name__ == 'Title':
                    category_id = int(row['category'])

                    try:
                        category = Category.objects.get(pk=category_id)
                    except Category.DoesNotExist:
                        self.stderr.write(self.style.ERROR(
                            f"Category with ID {category_id} not found.")
                        )
                        continue

                    row['category'] = category

                model.objects.update_or_create(**row)
        return None
