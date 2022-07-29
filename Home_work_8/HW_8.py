from datetime import datetime, timedelta

# list of users
users = [
    {"Anton": datetime(year=1989, month=7, day=30)},
    {"Vova": datetime(year=2003, month=8, day=2)},
    {"Ivan": datetime(year=1989, month=8, day=4)},
    {"Katja": datetime(year=1975, month=7, day=30)},
    {"Mykola": datetime(year=1985, month=8, day=1)},
    {"Oleg": datetime(year=1966, month=8, day=5)},
    {"Petro": datetime(year=1994, month=8, day=3)},
    {"Stepan": datetime(year=1984, month=8, day=1)},
    {"Pavlo": datetime(year=1982, month=8, day=3)},
    {"Sofija": datetime(year=1989, month=7, day=31)},
    {"Sergij": datetime(year=1994, month=7, day=3)},
]


def get_birthdays_per_week(users):

    # dictionary days of week
    days_name = {
        0: "Monday: ",
        1: "Tuesday: ",
        2: "Wednesday: ",
        3: "Thursday: ",
        4: "Friday: "
    }
    # cheking next weeks dates
    list_date = []
    for i in range(1, 8):
        future = datetime.now() + timedelta(days=i)
        list_date.append(future.strftime("%m-%d"))

    # verification of each user
    for user in users:

        for key, value in user.items():
            birhtday = value.strftime("%m-%d")

            # verification of birthday
            if birhtday in list_date:
                birhtday = str(datetime.now().year) + "-" + birhtday
                today = datetime.strptime(birhtday, '%Y-%m-%d')
                week_day = today.weekday()

                # checking weekdays
                if week_day < 5:
                    days_name[week_day] += key + ", "
                else:
                    days_name[0] += key + ", "

    return days_name


def main():
    days = get_birthdays_per_week(users)

    # printing users names with days
    for i in days:
        if len(days[i]) > 11:
            print(days[i])


if __name__ == '__main__':
    main()
