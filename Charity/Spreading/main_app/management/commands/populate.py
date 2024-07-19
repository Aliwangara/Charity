import json
import os.path

from django.core.management import BaseCommand

from Charity.Spreading.Spreading.settings import base
from main_app.models import Volunteers


class Command(BaseCommand):
    help = "Populate employees table with 1000 records"

    def handle(self, *args, **options):
        path = os.path.join(base.BASE_DIR, 'employees.json')
        self.stdout.write(
            self.style.SUCCESS("Started to import data")
        )
        with open(path) as file:  #files = open(path)
            employees = json.load(file)
            for e in employees:
                Volunteers.objects.create(
                    name = e['first_name'],
                    email = e['email'],
                    dob = e['dob'],
                    salary= e['salary'],
                    disabled= e['disabled'],
                )

        self.stdout.write(
            self.style.SUCCESS("Completed importing data")
    )
#         celery tasks
