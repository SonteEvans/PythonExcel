import random
import datetime

def random_date_time():
    # Generate a random year between 2024 and 2025
    year = random.randint(2024, 2024)

    # Generate a random month (1-12)
    month = random.randint(1, 12)

    # Generate a random day, considering the month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    else:  # February
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)

    # Generate random hour (0-23)
    hour = random.randint(0, 23)

    # Generate random minute (0-59)
    minute = random.randint(0, 59)

    # Generate random second (0-59)
    second = random.randint(0, 59)

    # Create a datetime object
    date_time = datetime.datetime(year, month, day, hour, minute, second)

    return date_time

# Generate and print a random date and time
random_datetime = random_date_time()
print(random_datetime)