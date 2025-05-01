from datetime import date, timedelta

from pendulum import duration

date1 = date(2020, 1, 1)
date2 = date(2021, 1, 1)

# access value
year = date1.year
month = date1.month
day = date1.day

weekday = date1.weekday()

# calculate
min_date = min(date1, date2)
max_date = max(date1, date2)

new_date = date1 + timedelta(days=1, seconds=0, minutes=0, hours=0, weeks=0)
date_duration = max_date - min_date

# format
iso = date.isoformat(new_date)
cus = date.strftime(new_date, "%Y-%m-%d on %H-%M-%S")

if __name__ == '__main__':
    print(year, month, day)
    print(weekday)

    print(date_duration)
    print(date_duration.days)

    print(iso)
    print(cus)

