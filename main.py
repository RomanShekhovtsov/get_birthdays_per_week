from datetime import datetime, timedelta

users = [{"name": "Roman", "birthday": "1995,02,20"},
         {"name": "Max", "birthday": "1995,02,21"},
         {"name": "Nikita", "birthday": "1995,02,22"},
         {"name": "Alex", "birthday": "1995,02,23"},
         {"name": "Vlad", "birthday": "1995,02,24"},
         {"name": "Diana", "birthday": "1995,02,25"},
         {"name": "Mickey", "birthday": "1995,02,26"},
         {"name": "Andrey", "birthday": "1995,02,27"}]

def get_birthdays_per_week (users):


    now_time = datetime.now()
    now_date = datatime.date()

    one_weeks_interval = timedelta(weeks=1)
    future_time_1 = now_data + one_weeks_interval

    Monday = []
    Tuesday = []
    Wednesday = []
    Thursday = []
    Friday = []

    for el in users:
        users_value = []
        for el_val in el.values():
            users_value.append(el_val)

        if now_data.month == users_value[1].month and now_data.day < users_value[1].day:

            t = calendar.weekday(future_time_1.year, users_value[1].month, users_value[1].day)

            if t == 5 or t == 6:
                t = 0

            if t == 0:
                monday.append(users_value[0])
            elif t == 1:
                tuesday.append(users_value[0])
            elif t == 2:
                wednesday.append(users_value[0])
            elif t == 3:
                thursday.append(users_value[0])
            elif t == 4:
                friday.append(users_value[0])

        if users_value[1].month == future_time_1.month and users_value[1].day < future_time_1.day:
            t = calendar.weekday(future_time_1.year, users_value[1].month, users_value[1].day)

            if t == 5 or t == 6:
                t = 0

            if t == 0:
                monday.append(users_value[0])
            elif t == 1:
                tuesday.append(users_value[0])
            elif t == 2:
                wednesday.append(users_value[0])
            elif t == 3:
                thursday.append(users_value[0])
            elif t == 4:
                friday.append(users_value[0])

    if monday != []:
        m = ", ".join(monday)
        print(f"Monday: {m}")
    if tuesday != []:
        tu = ", ".join(tuesday)
        print(f"Tuesday: {tu}")
    if wednesday != []:
        w = ", ".join(wednesday)
        print(f"Wednesday: {w}")
    if thursday != []:
        th = ", ".join(thursday)
        print(f"Thursday: {th}")
    if friday != []:
        f = ", ".join(friday)
        print(f"Friday: {f}")

    get_birthdays_per_week(users)