import datetime

from application import salary
from application.db import people
from datetime import datetime, date, time
from datetime import time

# def date_now():
#     current_date = date.today()
#     print(current_date)

def date_now_logger(function):
    def logger(*args, **kwargs):
        print('decor')
        function()
        result1 = date_now_logger(function)
        with open('C:\logs_python.txt', 'a', encoding='utf-8') as f:
            f.write(f'{datetime.now}, {function.__name__}, {result1} \n')
        return result1
    return logger

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    # date_now()
# @date_now_logger(r'C:\logs_python.txt')
@date_now_logger
def date_now():
    result = date.today()
    return print(result)
date_now()