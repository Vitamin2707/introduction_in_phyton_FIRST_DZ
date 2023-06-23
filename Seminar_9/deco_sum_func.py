"""
Объедините функции из прошлых задач. Функцию угадайку задекорируйте декораторами для сохранения параметров, декоратором
контроля значений и декоратором для многократного запуска. Выберите верный порядок декораторов.
"""

from deco_param import count
from two_numbers import two_numbers
from two_numbers_two import decorate
from multy import decorator_json


@count(3)
@decorator_json
def fact(num: int) -> int:
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


@count(3)
@decorator_json
def multy(a: int, b: int, *args, **kwargs):
    return a * b


@count(3)
@decorator_json
@decorate
def two_numbers_two(count_try: int, num: int):
    for i in range(1, count_try + 1):
        user_input = input(' Введите число для отгадывания от 1 до 100: ')
        if int(user_input) == num:
            print(f'Вы угадали с {i} попытки')
            break
    else:
        print('Вы не угадали')


if __name__ == '__main__':
    results = two_numbers(3, 20)
    print(results)
    results()
    two_numbers_two(11, 20)
    multy(6, 7, temp=2, res=3, c=2, d=5)
    print(fact(5))
