from csv import DictReader
from .models import User


def read_and_decode_csv(file, encoding='utf-8'):

    decoded_file = file.read().decode(encoding).splitlines()
    return decoded_file


def create_user_from_row(row):

    user = User(
        lietotajs=row['lietotajs'],
        epasts=row['epasts'],
    )

    user.save()


def lietotaji_csv_rows_to_db(file):

    csv_reader = DictReader(file)

    for row in csv_reader:
        create_user_from_row(row)