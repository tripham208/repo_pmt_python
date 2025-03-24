from datetime import datetime, timedelta

datetime1 = datetime(2020, 1, 1)
datetime2 = datetime(2021, 1, 1)

# access value
year = datetime1.year
month = datetime1.month
day = datetime1.day

weekday = datetime1.weekday()

# calculate
min_date = min(datetime1, datetime2)
max_date = max(datetime1, datetime2)

new_date = datetime1 + timedelta(days=1, seconds=0, minutes=0, hours=0, weeks=0)
date_duration = max_date - min_date

# format
iso = datetime.isoformat(new_date)
cus = datetime.strftime(new_date, "%Y-%m-%d on %H-%M-%S")

if __name__ == '__main__':
    print(year, month, day)
    print(weekday)

    print(date_duration)

    print(iso)
    print(cus)

