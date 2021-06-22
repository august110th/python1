from application import salary
from application.db import people
from datetime import datetime, date

def decorator(file):
     def logger(old_function):
         result_old = old_function(x)
         with open(file, 'a', encoding='utf-8') as f:
             f.write(f'функция запущена: {datetime.now()}, название функции: {old_function.__name__}, аргументы:{x}, результат: {result_old} \n')
         return old_function
     return logger

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    # date_now()
@decorator(r'C:\logs_python.txt')
def date_now(*args, **kwargs):
    result = date.today()
    return result
date_now(1)