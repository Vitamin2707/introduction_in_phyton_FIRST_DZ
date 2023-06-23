"""
Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
"""

import task


# def new_puzzle(puzzles: dict, try_count: int):
#     for key, val in puzzles.items():
#         try_count_1 = task.puzzle(key, val, try_count)
#         if try_count_1:
#             print(f"Угадано за {try_count_1} раза")
#         else:
#             print("Не угадали (")


"""
Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с 
которой она угадана). 
Функция формирует словарь с информацией о результатах отгадывания. 
Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде. 
Для формирования результатов используйте генераторное выражение.
"""
# import task

_ANSWEARS = dict()


def new_puzzle(puzzles: dict, try_count: int):
    for key, val in puzzles.items():
        try_count_1 = task.puzzle(key, val, try_count)
        if try_count_1:
            _ANSWEARS[key] = f"Угадано за {try_count_1} раза"
            print(f"Угадано за {try_count_1} раза")
        else:
            _ANSWEARS[key] = "Не угадали ("
            print("Не угадали (")


def show_result():
    print(*(f"{key} - {val}\n" for key, val in _ANSWEARS.items()))
