import csv
import os
from django.apps import apps
from django.core.management.base import BaseCommand, CommandError

from reviews.models import Category, Genre, Title


IMPORT_DATA = {
    'users': {
        'models': [
            'CustomUser'
        ],
        'csv_files': [
            'users.csv'
        ],
    },
    'reviews': {
        'models': [
            'Category',
            'Genre',
            'Title',
            'title_genre',
            'Review',
            'Comment'
        ],
        'csv_files': [
            'category.csv',
            'genre.csv',
            'titles.csv',
            'genre_title.csv',
            'review.csv',
            'comments.csv'
        ],
    },
}

FILE_PATH = '././static/data/'


class Command(BaseCommand):
    help = 'Import CSV data to a Django model'

    def add_arguments(self, parser):
        parser.add_argument(
            '--app',
            type=str,
            help='Name of the Django app containing the model.'
        )

        parser.add_argument(
            '--model',
            type=str,
            help='Name of the Django model(s). Can be specified multiple times.'
        )

        parser.add_argument(
            '--file',
            type=str,
            help='Path to the CSV file(s). Can be specified multiple times.'
        )

    def check_input(self, app, model=None, file=None):
        app_names = [app_config.name for app_config in apps.get_app_configs()]
        if app in app_names:  # Проверяем существование app в приложениях
            if model:  # Если передан model -> проверка существования
                try:
                    model = apps.get_model(
                        app_label=app,
                        model_name=model
                    )
                except LookupError:
                    raise CommandError(f'App "{app}" '
                                       f'doesn`t have model "{model}"')
        else:
            raise CommandError(f'App: {app} doesn`t exists')

        if file:  # Проверяем, задан ли файл
            if not os.path.exists(file):
                raise CommandError(f'File: {file} doesn`t exists '
                                   f'at {FILE_PATH}')

        return True

    def insert(self, app, model, file):
        pass

    def handle(self, *args, **options):
        '''Отрабатывает импорт данных.'''
        '''
        Если переданы аргументы app, model, file -> точечная вставка.
        Если передан аргумент app -> произвести вставку по заготовленным
        пресетам для приложения.
        Если аргументы не переданы -> вставка по пресету:
        приложение - модель - файл
        '''
        app_name = options['app']
        model_name = options['model']
        csv_file = os.path.join(FILE_PATH, options['file'])
        print(app_name, model_name, csv_file)
        print(self.check_input(app_name, model_name, csv_file))
        if app_name is None and model_name is None and csv_file is None:
            return ('All is None')
        for model_name, csv_file in zip(model_name, csv_file):

            try:
                model = apps.get_model(
                    app_label=app_name,
                    model_name=model_name
                )
                print(model.__name__, app_name)
            except LookupError:
                self.stderr.write(self.style.ERROR(
                    f'Model "{model_name}" not found in app "{app_name}".'
                ))
                continue

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

