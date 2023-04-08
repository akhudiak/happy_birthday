from collections import defaultdict
from datetime import datetime, date, timedelta
from get_data import get_name, get_birthday


def create_users(count):

    users = []

    for _ in range(count):
        users.append({"name": get_name(), "birthday": get_birthday()})

    return users


def get_birthdays_per_week(users):

    birthdays_dct = defaultdict(list)
    current_date = date.today()
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    for user in users:

        current_birthday = user["birthday"].replace(year=current_date.year)
        week_day = current_birthday.strftime("%A")

        if week_day in ["Saturday", "Sunday"]:
            week_day = "Monday"

        if current_date <= current_birthday <= current_date + timedelta(days=7):
            birthdays_dct[week_day].append(user["name"])

    for weekday in weekdays:
        names = ", ".join(birthdays_dct[weekday])
        if names:
            print(f"{weekday}: {names}")


if __name__ == "__main__":

    count = 20
    users = create_users(count)

# debug list
    # users = [{'birthday': date(1996, 4, 17), 'name': 'Ashley Coffey'},
    # {'birthday': date(1995, 4, 15), 'name': 'Jeremy Holden'},
    # {'birthday': date(1997, 4, 12), 'name': 'James Mccullough'},
    # {'birthday': date(1979, 4, 15), 'name': 'Chris Smith'},
    # {'birthday': date(1984, 4, 23), 'name': 'Justin Zamora'},
    # {'birthday': date(1985, 4, 13), 'name': 'Zachary Rodriguez'},
    # {'birthday': date(1997, 4, 18), 'name': 'Teresa Bradley'},
    # {'birthday': date(1983, 4, 4), 'name': 'Carolyn Villarreal'},
    # {'birthday': date(1987, 4, 9), 'name': 'Joshua Lee'},
    # {'birthday': date(1992, 4, 1), 'name': 'Bradley Robinson'},
    # {'birthday': date(1982, 4, 3), 'name': 'Sherri Willis'},
    # {'birthday': date(1998, 4, 25), 'name': 'Zachary Ward'},
    # {'birthday': date(1979, 4, 4), 'name': 'Alan Miller'},
    # {'birthday': date(1993, 4, 22), 'name': 'Leroy Collins'},
    # {'birthday': date(1987, 4, 2), 'name': 'Sandra Turner'},
    # {'birthday': date(1979, 4, 24), 'name': 'Tiffany Walker'},
    # {'birthday': date(1998, 4, 14), 'name': 'Lauren Perry'},
    # {'birthday': date(1990, 4, 12), 'name': 'Tracy Mitchell'},
    # {'birthday': date(1976, 4, 4), 'name': 'Trevor Monroe'},
    # {'birthday': date(1994, 4, 18), 'name': 'Eric Cooper'}]

    get_birthdays_per_week(users)