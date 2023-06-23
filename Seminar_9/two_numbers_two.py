"""
Дорабатываем задачу 1. Превратите внешнюю функцию в декоратор. Он должен проверять входят ли переданные в
функцию-угадайку числа в диапазоны [1, 100] и [1, 10]. Если не входят,
вызывать функцию со случайными числами из диапазонов.
"""
import random
from typing import Callable


def decorate(func: Callable):
    MIN_COUNT = 1
    MAX_COUNT = 10
    MIN_NUM = 1
    MAX_NUM = 100

    def wrapper(*args):
        input_count, input_num = args
        if MIN_COUNT > input_count or input_count > MAX_COUNT:
            input_count = random.randint(MIN_COUNT, MAX_COUNT)
        # if MIN_NUM > input_num or input_num > MAX_NUM:
        if MIN_NUM > input_num or input_num > MAX_NUM:
            input_num = random.randint(MIN_NUM, MAX_NUM)
        return func(input_count, input_num)

    return wrapper


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
    two_numbers_two(11, 20)
