#Задание 7

from datetime import datetime, timedelta, date
def third_wednesday(dt):
    first_day = dt.replace(day = 1)
    offset = (2 - first_day.weekday()) % 7
    first_wednesday = first_day + timedelta(days = offset)
    return (first_wednesday + timedelta(days = 14)).date()

print(third_wednesday(datetime(2024,1,15)))