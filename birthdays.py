from datetime import datetime, timedelta
from collections import defaultdict


users = [{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
         {"name": "Anna Family", "birthday": datetime(2003, 3, 3)},
         {"name": "Mary Phisher", "birthday": datetime(2003, 10, 14)},
         {"name": "Tony Harryson", "birthday": datetime(2003, 10, 15)},
         {"name": "Kaleb Family", "birthday": datetime(2003, 10, 16)},
         {"name": "Din Nerest", "birthday": datetime(2003, 10, 16)},
         {"name": "Sem Nester", "birthday": datetime(2003, 10, 20)},
         {"name": "Ed Nester", "birthday": datetime(2003, 10, 21)},
         {"name": "Tom Adding", "birthday": datetime(1955, 9, 30)},
         {"name": "James Evans", "birthday": datetime(1975, 1, 12)},
         {"name": "Harry Potter", "birthday": datetime(1980, 7, 31)}]

days_of_week = {
    0 : 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

def get_birthdays_per_week(users):
    week_birthdays = defaultdict(list)
    this_day = datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=this_day.year)
        if birthday_this_year < this_day:
            birthday_this_year = birthday.replace(year=(this_day.year+1))
        if (birthday_this_year - this_day) < timedelta(days = 7):
            day = birthday_this_year.weekday()
            week_birthdays[day].append(name)
    week_birthdays = sorted(week_birthdays.items())
    this_day_of_week = this_day.weekday()
    print(week_birthdays)


if __name__ == "__main__":
    get_birthdays_per_week(users)
