"""

Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит
 уникальные (без повтора) элементы исходного списка.
*Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков

Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов
 ниже:
целое положительное число
вещественное положительное или отрицательное число
строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
строку в верхнем регистре в остальных случаях

"""


def uniq(numbers: list) -> list:
    result = []
    for i in numbers:
        if i not in result:
            result.append(i)
    return result


def uniq2(numbers: list) -> list:
    return list(set(numbers))


def reformat1(text: str) -> (int, float, str):
    result = None
    if text.isdigit():
        if "." not in text:
            result = int(text)
        else:
            result = float(text)
    elif text.istitle():
        result = text.lower()
    else:
        result = text.upper()

    return result


def reformat2(text: str) -> (int, float, str):
    result = None
    if "." in text or (text.count("-") and text.index("-") == 0):
        result = float(text)
    elif text.isdigit():
        result = int(text)
    elif text.lower() != text:
        result = text.lower()
    else:
        result = text.upper()

    return result


def get_type_dict(corteg: tuple) -> dict:
    result = {}
    for i in corteg:
        result.setdefault(type(i), []).append(i)
    return result


def my_list_index(mylist: list[int]) -> list[int]:
    return [i for i, j in filter(lambda x: x[1] % 2 != 0, enumerate(mylist, 1))]
