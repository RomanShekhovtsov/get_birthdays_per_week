from datetime import datetime, timedelta
import calendar

users = [
    {"name": "Roman", "birthday": "1995,02,20"},
    {"name": "Max", "birthday": "1995,02,21"},
    {"name": "Nikita", "birthday": "1995,02,22"},
    {"name": "Alex", "birthday": "1995,03,23"},
    {"name": "Vlad", "birthday": "1995,04,24"},
    {"name": "Diana", "birthday": "1995,05,25"},
    {"name": "Mickey", "birthday": "1995,06,26"},
    {"name": "Andrey", "birthday": "1995,07,27"}
]

def get_birthdays_per_week(users):
    now_date = datetime.now().date()
    one_weeks_interval = timedelta(weeks=1)
    future_date = now_date + one_weeks_interval

    Monday = []
    Tuesday = []
    Wednesday = []
    Thursday = []
    Friday = []

    for el in users:
        users_value = list(el.values())

        if now_date.month == users_value[1].month and now_date.day < users_value[1].day:
            t = calendar.weekday(future_date.year, users_value[1].month, users_value[1].day)

            if t == 5 or t == 6:
                t = 0

            if t == 0:
                Monday.append(users_value[0])
            elif t == 1:
                Tuesday.append(users_value[0])
            elif t == 2:
                Wednesday.append(users_value[0])
            elif t == 3:
                Thursday.append(users_value[0])
            elif t == 4:
                Friday.append(users_value[0])

        if users_value[1].month == future_date.month and users_value[1].day < future_date.day:
            t = calendar.weekday(future_date.year, users_value[1].month, users_value[1].day)

            if t == 5 or t == 6:
                t = 0

            if t == 0:
                Monday.append(users_value[0])
            elif t == 1:
                Tuesday.append(users_value[0])
            elif t == 2:
                Wednesday.append(users_value[0])
            elif t == 3:
                Thursday.append(users_value[0])
            elif t == 4:
                Friday.append(users_value[0])

    if Monday:
        m = ", ".join(Monday)
        print(f"Monday: {m}")
    if Tuesday:
        tu = ", ".join(Tuesday)
        print(f"Tuesday: {tu}")
    if Wednesday:
        w = ", ".join(Wednesday)
        print(f"Wednesday: {w}")
    if Thursday:
        th = ", ".join(Thursday)
        print(f"Thursday: {th}")
    if Friday:
        f = ", ".join(Friday)
        print(f"Friday: {f}")

get_birthdays_per_week(users)
