from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from firstapp.models import Admission, Vaccine
from pytz import UTC


DATETIME_FORMAT = '%Y'

VACCINES_NAMES = [
    'Moderna',
'Sinopharm',
'SinoVac',
'Pfizer'
]

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from school_data.csv into our app "

    def handle(self, *args, **options):
        if Vaccine.objects.exists() or Admission.objects.exists():
            print('Student data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Creating vaccine data")
        for vaccine_name in VACCINES_NAMES:
            vac = Vaccine(name=vaccine_name)
            vac.save()
        print("Loading student data for students available for admission")
        for row in DictReader(open('./school_data.csv')):
            student = Admission()
            student.name = row['Name']
            student.father_name = row['Father Name']
            student.city = row['City']
            student.score = row['Score']
           
            student.sex = row['Sex']
            raw_submission_date = row['Birth Date']
            submission_date = UTC.localize(
            datetime.strptime(raw_submission_date, DATETIME_FORMAT))
            student.birth_date = submission_date
            student.age = row['Age']
            
            student.save()
            raw_vaccination_names = row['Vaccinations']
            vaccination_names = [name for name in raw_vaccination_names.split('| ') if name]
            for vac_name in vaccination_names:
                vac = Vaccine.objects.get(name=vac_name)
                student.vaccinations.add(vac)
            student.save()
