from datetime import datetime, timedelta
from collections import defaultdict


users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Anna Family", "birthday": datetime(2003, 3, 3)},
    {"name": "Mary Phisher", "birthday": datetime(2003, 10, 14)},
    {"name": "Ed Nester", "birthday": datetime(2003, 10, 21)},
    {"name": "Tony Harryson", "birthday": datetime(2003, 10, 15)},
    {"name": "Kaleb Family", "birthday": datetime(2003, 10, 16)},
    {"name": "Din Nerest", "birthday": datetime(2003, 10, 16)},
    {"name": "Sem Nester", "birthday": datetime(2003, 10, 20)},
    {"name": "Tom Adding", "birthday": datetime(1955, 9, 30)},
    {"name": "James Evans", "birthday": datetime(1975, 1, 12)},
    {"name": "Harry Potter", "birthday": datetime(1980, 7, 31)},
]

days_of_week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


def sorted_birthdays(today, birthdays_dict):
    befor_today = [i for i in range(7) if i >= today]
    after_today = [j for j in range(7) if j < today]
    desired_order = befor_today + after_today
    sorted_data = {}
    for key in desired_order:
        if key in birthdays_dict:
            sorted_data[key] = birthdays_dict[key]
    return sorted_data


def get_birthdays_per_week(users):
    week_birthdays = defaultdict(list)
    this_day = datetime.today().date()
    this_day_of_week = this_day.weekday()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=this_day.year)
        if birthday_this_year < this_day:
            birthday_this_year = birthday.replace(year=(this_day.year + 1))
        if (birthday_this_year - this_day) < timedelta(days=7):
            day = birthday_this_year.weekday()
            # якщо сьгодні не понеділок, переносимо дні народження з вихідних на наступний понеділок
            if day > 4 and this_day_of_week > 0:
                week_birthdays[0].append(name)
            # якщо сьгодні понеділок - не виводимо дні народження які припадаюь на вихідні
            elif day > 4 and this_day_of_week == 0:
                continue
            # робочі дні записуємо самі в себе
            else:
                week_birthdays[day].append(name)

    sorted_week_birthdays = sorted_birthdays(this_day_of_week, week_birthdays)
    for key in sorted_week_birthdays.keys():
        day_name = days_of_week[key]
        str_of_names = ", ".join(sorted_week_birthdays[key])
        print(f"{day_name}: {str_of_names}")


if __name__ == "__main__":
    get_birthdays_per_week(users)
