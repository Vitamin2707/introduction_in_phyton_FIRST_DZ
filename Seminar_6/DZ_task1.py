"""В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку."""
from sys import argv

from Seminar_6 import date_validate


def check_date(date: list) -> bool:
    def find_sep(str_date: str) -> str:
        for char in str_date:
            if not char.isdigit():
                return char

    if len(date) == 1:
        day, month, year = tuple(map(int, date[0].split(find_sep(date[0]))))
    else:
        day, month, year = tuple(map(int, date))
    if 0 < month < 13 and 0 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if not 0 < day < 32:
                return False
        elif month in [4, 6, 9, 11]:
            if not 0 < day < 31:
                return False
        else:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                if not 0 < day < 30:
                    return False
            else:
                if not 0 < day < 29:
                    return False
    else:
        return False
    return True


if __name__ == '__main__':
    data = '12.01.2000'
    print(date_validate.date_validator(data))

    # name, *args = argv
    # print('Верная дата' if check_date(args) else 'Такой даты не может быть')
