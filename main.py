from application import salary
from application.db import people
from datetime import datetime, date

def date_now():
    result = date.today()
    return print(result)
def decorator(old_function):
     def logger():
         log_some = old_function()
         with open('file', 'a', encoding='utf-8') as f:
             log_some = f.write(f'функция запущена: {datetime.now()}, название функции: {old_function.__name__}, параметры:, результат: {log_some} \n')
            return log_some
     return logger()


if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    date_now()
# # @decorator(r'C:\Users\User\Pictures\logs.txt')
