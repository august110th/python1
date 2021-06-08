from application import salary
from application.db import people
from datetime import date

# def date_now():
#     current_date = date.today()
#     print(current_date)

def date_now_logger(function):
    def logger():
        print('decor')
        result = function()
        return result
    return logger



if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    # date_now()
@date_now_logger
def date_now():
    current_date = date.today()
    print(current_date)
