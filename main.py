from application import salary
from application.db import people
from datetime import datetime

def date_now():
    current_datetime = datetime.now()
    print(current_datetime)


if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    date_now()