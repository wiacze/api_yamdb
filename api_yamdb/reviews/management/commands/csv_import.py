import csv

from django.apps import apps
from django.core.management.base import BaseCommand

from reviews.models import Category, Genre, Title


class Command(BaseCommand):
    help = 'Import CSV data to a Django model'

    def add_arguments(self, parser):
        parser.add_argument(
            'app_name',
            type=str,
            default='reviews',
            help='Name of the Django app containing the model.'
        )
        parser.add_argument(
            'model_name',
            nargs='*',
            type=str,
            default=[
                'category',
                'genre',
                'title',
                'title_genre',
            ],
            help='Name of the Django model.'
        )
        parser.add_argument(
            'csv_file',
            nargs='*',
            type=str,
            default=[
                'category.csv',
                'genre.csv',
                'titles.csv',
                'genre_title.csv',
            ],
            help='Path to the CSV file.'
        )

    def handle(self, *args, **options):
        app_name = options['app_name']
        model_names = options['model_name']
        csv_files = options['csv_file']

        for model_name, csv_file in zip(model_names, csv_files):
            file_path = f'././static/data/{csv_file}'

            try:
                model = apps.get_model(
                    app_label=app_name,
                    model_name=model_name
                )
            except LookupError:
                self.stderr.write(self.style.ERROR(
                    f'Model "{model_name}" not found in app "{app_name}".'
                ))
                continue

            with open(file_path, 'r', encoding='utf-8') as csvfile:
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
