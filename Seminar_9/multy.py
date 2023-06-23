"""
Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает.
При повторном вызове файл должен расширяться, а не перезаписываться.
●	Каждый ключевой параметр сохраните как отдельный ключ json словаря.
●	Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
●	Имя файла должно совпадать с именем декорируемой функции.
"""
import json
import os
from typing import Callable, Any


def decorator_json(func: Callable):
    def wrapper(*args, **kwargs) -> Any:
        # os.path.exists(path) - возвращает True, если path указывает на существующий путь или дескриптор открытого
        # файла.
        # os.path.getsize(path) - размер файла в байтах.
        if os.path.exists(func.__name__) and os.path.getsize(f'data/{func.__name__}.json') > 0:
            with open(f'data/{func.__name__}.json', 'r', encoding='utf-8') as f_in:
                data = json.load(f_in)
            data.append({})
        else:
            data = [{'args': {}, 'kwargs': {}, 'result': None}]
        if args:
            data[-1]['args'] = {f'arg{i}': args[i] for i in range(len(args))}
        if kwargs:
            data[-1]['kwargs'] = kwargs
        result = func(*args, **kwargs)
        data[-1]['result'] = result
        func(*args, **kwargs)
        with open(f'data/{func.__name__}.json', 'w', encoding='utf-8') as f_js:
            json.dump(data, f_js, indent=2)
            print(f'Файл с именем декорируемой функции data/{func.__name__}.json сохранен')

    return wrapper


@decorator_json
def multy(a: int, b: int, *args, **kwargs):
    return a * b


# import json
# from typing import Callable


# def deco(func: Callable):
#     with open(f'{func.__name__}.json', 'r') as f:
#         final_dict = json.load(f)
#
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         # for i in range(len(args)):
#         final_dict.update({str(res): args[res]})
#         final_dict.update({**kwargs})
#         with open(f'{func.__name__}.json', 'w') as f_j:
#             json.dump(final_dict, f_j, indent=2)
#
#     return wrapper
#
#
# @deco
# def multy(a: int, b: int, *args, **kwargs):
#     return a * b


if __name__ == '__main__':
    multy(6, 7, temp=2, res=3, c=2, d=5)
