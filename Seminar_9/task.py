"""Создайте функцию-замыкание, которая запрашивает два целых числа:
●	от 1 до 100 для загадывания,
●	от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток."""


from typing import Callable


def two_numbers(count_try: int, num: int) -> Callable[[], None]:
    def random_numbers():
        for i in range(1, count_try + 1):
            user_input = input('Введите число для отгадывания от 1 до 100: ')
            if int(user_input) == num:
                print(f'Вы угадали с {i} попытки')
                break
        else:
            print('Вы не угадали')

    return random_numbers


res = two_numbers(3, 20)
res()


def deco(func: Callable):
    MIN_COUNT = 1
    MAX_COUNT = 10
    MIN_NUM = 1
    MAX_NUM = 100

    def wrapper(*args, **kwargs):
        input_count, input_num = args
        if MIN_COUNT > input_count or input_count > MAX_COUNT:
            input_count = random.randint(MIN_COUNT, MAX_COUNT)
        if MIN_NUM > input_num or input_num > MAX_NUM:
            input_num = random.randint(MIN_NUM, MAX_NUM)
        return func(input_count, input_num)

    return wrapper


mport json
from typing import Callable


def deco(func: Callable):
    with open(f'{func.__name__}.json', 'r') as f:
        final_dict = json.load(f)

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        for i in range(len(args)):
            final_dict.update({str(i): args[i]})
        final_dict.update({**kwargs})
        with open(f'{func.__name__}.json', 'w') as f:
            json.dump(final_dict, f, indent=2)

    return wrapper


@deco
def multy(a: int, b: int, *args, **kwargs) -> int:
    return a * b


multy(6, 7, temp=2, res=3, c=2, d=5)