# datetime package

import datetime as dt

date_input = '29.11.2022'
time_input = '18:44'
date_format = '%d.%m.%Y'
time_format = '%H:%M'

list_of_dates = ['13.01.1990', '28.02.2022', '19.07.1980', '31.12.2025']
list_of_times = ['14:59', '3:17', '12:09', '19:04']


def get_date():
    return dt.date.today()


def set_date(year, month, day):
    return dt.date.fromisocalendar(year, month, day)


def get_datetime():
    return dt.datetime.today()


def get_year():
    x = dt.datetime.now()
    return x.year


def get_month():
    x = dt.datetime.now()
    return x.month


def get_day():
    x = dt.datetime.now()
    return x.day


def get_weekday():
    x = dt.datetime.now()
    return x.strftime('%a')


def get_weekday_full():
    x = dt.datetime.now()
    return x.strftime('%A')


def get_weekday_as_num():
    x = dt.datetime.now()
    return x.strftime('%w')


def get_day_of_month():
    x = dt.datetime.now()
    return x.strftime('%d')


def get_month_num():
    x = dt.datetime.now()
    return x.strftime('%b')


def get_month_full():
    x = dt.datetime.now()
    return x.strftime('%B')


def get_month_as_num():
    x = dt.datetime.now()
    return x.strftime('%m')


def get_year_short():
    x = dt.datetime.now()
    return x.strftime('%y')


def get_year_full():
    x = dt.datetime.now()
    return x.strftime('%Y')


def get_hour_24h():
    x = dt.datetime.now()
    return x.strftime('%H')


def get_hour_12h():
    x = dt.datetime.now()
    return x.strftime('%l')


def get_am_pm():
    x = dt.datetime.now()
    return x.strftime('%p')


def get_minutes():
    x = dt.datetime.now()
    return x.strftime('%M')


def get_seconds():
    x = dt.datetime.now()
    return x.strftime('%S')


def get_microseconds():
    x = dt.datetime.now()
    return x.strftime('%f')


def get_timezone():
    x = dt.datetime.now()
    return x.strftime('%Z')


def get_day_num():
    x = dt.datetime.now()
    return x.strftime('%j')


def get_week_num():
    x = dt.datetime.now()
    return x.strftime('%U')


def get_century():
    x = dt.datetime.now()
    return x.strftime('%C')


def get_local_version_datetime():
    x = dt.datetime.now()
    return x.strftime('%c')


def get_local_version_time():
    x = dt.datetime.now()
    return x.strftime('%X')


def get_local_version_date():
    x = dt.datetime.now()
    return x.strftime('%x')


def make_custom_date():
    x = dt.datetime.now()
    return x.strftime('%d.%m.%Y r.')


def make_custom_date_with_weekday():
    x = dt.datetime.now()
    return x.strftime('%a, %d.%m.%Y r.')


def make_day_announcement():
    x = dt.datetime.now()
    return f'ELO! Dzisiaj jest {x.strftime("%d.%m.%Y r.")}'


def make_time_announcement():
    x = dt.datetime.now()
    return f'ELO! Mamy godzinę {x.strftime("%H:%M")}.'


def count_day_and_week():
    x = dt.datetime.now()
    return f'ELO! Mamy dzisiej {x.strftime("%j")} dzień roku i {x.strftime("%U")} tydzień roku.'


def get_tomorrow():
    return dt.date.today() + dt.timedelta(days=1)


def get_next_year():
    return dt.date.today() + dt.timedelta(weeks=52)


def get_next_year_weekday():
    x = dt.date.today() + dt.timedelta(weeks=52)
    return f'Za rok dzisiaj będzie {x.strftime("%a")}.'


def get_specific_weekday(year, month, day):
    x = dt.date(year, month, day)
    return x.strftime("%A")


def replace_day_in_datetime(day):
    x = dt.date.today()
    return x.replace(day=day)


def replace_month_in_datetime(mon):
    x = dt.date.today()
    return x.replace(month=mon)


def replace_year_in_datetime(year):
    x = dt.date.today()
    return x.replace(year=year)


def get_yesterday():
    return dt.date.today() - dt.timedelta(days=1)


def get_plus_one_hour():
    return dt.datetime.now() + dt.timedelta(hours=1)


def get_minus_x_hours(hours):
    return dt.datetime.now() - dt.timedelta(hours=hours)


def get_date_from_str(input, format):
    x = dt.datetime.strptime(input, format)
    return x.date()


def get_time_from_str(input, format):
    x = dt.datetime.strptime(input, format)
    return x.time()


def reformat_to_american_time(input, format):
    x = dt.datetime.strptime(input, format)
    return x.strftime('%m/%d/%y')


def create_date_objects_from_list(some_list, format):
    return [dt.datetime.strptime(item, format) for item in some_list]


def create_time_objects_from_list(some_list, format):
    return [dt.datetime.strptime(item, format) for item in some_list]


t = create_time_objects_from_list(list_of_times, time_format)
print(t)



# strptime
# timedelta
