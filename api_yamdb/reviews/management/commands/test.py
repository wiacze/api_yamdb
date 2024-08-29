import csv
import os
from django.apps import apps
from django.core.management.base import BaseCommand, CommandError


FILE_PATH = '././static/data/'


class Command():
    def add_arguments(self, parser):
        pass

    def check_input(self, app, model, file):
        if app:
            app_names = [
                app_config.name for app_config in apps.get_app_configs()
            ]
            if app in app_names:
                if model:
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

        if file:
            if not os.path.exists(file):
                raise CommandError(f'File: {file} doesn`t exists '
                                   f'at {FILE_PATH}')

        return True

    def insert(self, app, data):
        app_config = apps.get_app_config(app)

        for model_name in data['models']:
            model = app_config.get_model(model_name)

            for csv_file_name in data['csv_files']:
                csv_file = os.path.join(FILE_PATH, csv_file_name)
                with open(csv_file, 'r', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile)

                    for row in reader:
                        model.objects.update_or_create(**row)