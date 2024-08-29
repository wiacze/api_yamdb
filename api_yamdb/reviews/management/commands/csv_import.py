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

    def insert(self):
        for app_name, app_data in IMPORT_DATA.items():
            # Получаем приложение
            app_config = apps.get_app_config(app_name)

            # Проходим по моделям приложения
            for model_name in app_data['models']:
                model = app_config.get_model(model_name)

                # Проходим по CSV-файлам
                for csv_file_name in app_data['csv_files']:
                    # Формируем путь к CSV-файлу
                    csv_file = os.path.join(FILE_PATH, csv_file_name)

                    # Проверяем наличие файла
                    if not os.path.exists(csv_file):
                        raise CommandError(f"File {csv_file_name} not found in {FILE_PATH}")

                    # Открываем CSV-файл
                    with open(csv_file, 'r', encoding='utf-8') as csvfile:
                        reader = csv.DictReader(csvfile)

                        # Загружаем данные в модель
                        for row in reader:
                            # Создаем экземпляр модели
                            obj = model(**row)

                            # Сохраняем объект
                            obj.save()


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
        file_name = options['file']
        csv_file = os.path.join(FILE_PATH, options['file'])

