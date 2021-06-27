from application import salary
from application.db import people
from datetime import datetime, date

def decorator(file):
    def logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(file, 'a', encoding='utf-8') as f:
                f.write(f'функция запущена: {datetime.now()}, название функции: {old_function.__name__}, аргументы:{args, kwargs}, результат: {result} \n')
            return result
        return new_function
    return logger

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    # date_now()

@decorator(r'C:\Users\august110th\Documents\logs_python.txt')
def date_now(*args, **kwargs):
    result = date.today()
    return result

date_now(5,9, b='for')
