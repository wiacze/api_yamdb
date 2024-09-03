import csv
import os

from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from reviews.models import Category


User = get_user_model()

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
            help='Name of the Django model.'
        )

        parser.add_argument(
            '--file',
            type=str,
            help='Name CSV file.'
        )

    def check_input(self, app, model, file):
        if app:
            if app not in [
                app_config.name for app_config in apps.get_app_configs()
            ]:
                raise CommandError(f'App: {app} doesn`t exists')
            self.stderr.write(self.style.WARNING(
                f'Приложение "{app}" найдено!'
            ))
            if model:
                try:
                    apps.get_model(app_label=app, model_name=model)
                    self.stderr.write(self.style.WARNING(
                        f'Модель "{model}" в приложении "{app}" найдена!'
                    ))
                except LookupError:
                    raise CommandError(f'App "{app}" doesn`t have '
                                       f'model "{model}"')

        if file and not os.path.exists(os.path.join(FILE_PATH, file)):
            raise CommandError(f'File: "{file}" doesn`t exists '
                               f'at "{FILE_PATH}"')
        self.stderr.write(self.style.WARNING(
            f'Файл "{file}" найден!'
        ))

        return True

    def insert(self, app, data):
        app_config = apps.get_app_config(app)

        if len(data['models']) != len(data['csv_files']):
            raise ValueError(
                "Списки models и csv_files должны быть одинаковой длины"
            )

        for i in range(len(data['models'])):
            model_name = data['models'][i]
            csv_file_name = data['csv_files'][i]

            model = app_config.get_model(model_name)
            csv_file = os.path.join(FILE_PATH, csv_file_name)

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
                    elif model.__name__ in ('Review', 'Comment'):
                        user_id = int(row['author'])

                        try:
                            user = User.objects.get(pk=user_id)
                        except User.DoesNotExist:
                            self.stderr.write(self.style.ERROR(
                                f"User with ID {user_id} not found.")
                            )
                            continue

                        row['author'] = user

                    obj, created = model.objects.get_or_create(**row)
            self.stderr.write(self.style.SUCCESS(
                f'Данные из "{csv_file_name}" '
                f'импортированы в "{model_name}"'
            ))

    def handle(self, *args, **options):
        """Отрабатывает импорт данных."""
        """
        Если переданы аргументы app, model, file -> точечная вставка.
        Если передан аргумент app -> произвести вставку по заготовленным
        пресетам для приложения.
        Если аргументы не переданы -> вставка по пресету:
        приложение - модель - файл
        """
        app_name = options['app']
        model_name = options['model']
        file_name = options['file']
        if app_name and model_name and file_name:
            self.check_input(app_name, model_name, file_name)
            self.insert(
                app_name,
                {'models': [model_name],
                 'csv_files': [file_name]}
            )
        elif app_name and not model_name and not file_name:
            if app_name in IMPORT_DATA:
                current_data = IMPORT_DATA[app_name]
                for i in range(len(current_data['models'])):
                    self.check_input(
                        app_name,
                        current_data['models'][i],
                        current_data['csv_files'][i]
                    )
                self.insert(app_name, current_data)
        else:
            for app, data in IMPORT_DATA.items():
                for i in range(len(data['models'])):
                    self.check_input(
                        app,
                        data['models'][i],
                        data['csv_files'][i]
                    )
                self.insert(app, data)
