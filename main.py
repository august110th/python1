import datetime
from application import salary
from application.db import people
from datetime import datetime, date


def date_now_logger(function):
    def logger(**kwargs):
        result1 = function()
        with open('C:\logs_python.txt', 'a', encoding='utf-8') as f:
            f.write(f'функция запущена: {datetime.now()}, название функции: {function.__name__}, параметры: {kwargs}, результат: {result1} \n')
        return result1
    return logger

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
     # date_now()
@date_now_logger(r'C:\logs_python.txt')
def date_now():
    result = date.today()
    return result
date_now(x=1)