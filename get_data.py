from datetime import datetime, timedelta
import random

from faker import Faker


def get_name():
    return Faker().name()


def get_birthday():

    current_date = datetime.now()
    oldest_date = current_date - timedelta(days=365*50)

    while True:

        fake_year = random.randrange(oldest_date.year, current_date.year - 18)
        fake_month = 4 # random.randint(1, 12)
        fake_day = random.randint(1, 31)

        try:
            fake_birthday = datetime(fake_year, fake_month, fake_day)
            return fake_birthday.date()
        except ValueError:
            continue


if __name__ == "__main__":
    for _ in range(10):
        print(get_name(), get_birthday())