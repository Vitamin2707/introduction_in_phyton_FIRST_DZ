"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
"""
import os


def file_info(file_path):
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return path, name, extension


"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, 
премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве ключа и суммой премии 
в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии
"""


def premium(names: list[str], cash: list[int], percent: list[str]) -> dict[str:float]:
    return {name: money / 100 * perc
            for name, money, perc in zip(names, cash, (float(i[:-1]) for i in percent))}


"""
Создайте функцию генератор чисел Фибоначчи (см. Википедию)
"""


def hibachi(number: int) -> (iter, int):
    fibo_list = [0, 1, 1]
    current_number = 0
    while current_number < number:
        while len(fibo_list) < number:
            fibo_list.append(sum(fibo_list[-2:]))
        yield fibo_list[current_number]
        current_number += 1


def run():
    print(file_info(r'C:\Users\Артур\Final_Pyithon\HW1\Seminar_5\HW_5.py'))
    names = ["Andrew", "Stanis", "Artur"]
    cash = [722, 411, 333]
    percent = ["10.25%", "22.55%", "33.35%"]
    print(premium(names, cash, percent))
    print(*(hibachi(25)))


if __name__ == "__main__":
    run()
