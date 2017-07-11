from random import randint

days_in_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def generate_random_date():
    day = randint(1, 31)
    month = randint(1, 12)
    year = randint(1600, 2018)
    day_in_week = days_in_week[randint(0, 6)]
    hour = randint(1, 12)
    minute = randint(0, 59)
    am_or_pm = 'am' if randint(0, 1) == 0 else 'pm'
    return '{day}-{month}-{year}, {day_in_week}, {hour}:{minute}{am_or_pm}'.format(
        day=day,
        month=month,
        year=year,
        day_in_week=day_in_week,
        hour=hour,
        minute=minute,
        am_or_pm=am_or_pm
    )


def generate_dates(amount):
    dates = []
    for i in range(0, amount):
        dates.append(generate_random_date())
    return dates
