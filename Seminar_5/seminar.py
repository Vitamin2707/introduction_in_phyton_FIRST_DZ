"""
Задание №1
✔ Пользователь вводит строку из четырёх или более целых чисел, разделённых символом `“/”`.
Сформируйте словарь, где:
✔второе и третье число являются ключами.
✔первое число является значением для первого ключа.
✔четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа.
"""
from typing import Any, Generator

nums = '1/2/3/4/5/2/1'


def dict_with_int(texts: str) -> dict[int:int]:
    first, second, third, *another = (int(item) for item in texts.split("/"))
    return {second: first, third: tuple(another)}


print(dict_with_int(nums), '\n')

"""
Задание №2
✔ Самостоятельно сохраните в переменной строку текста.
✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
✔ Напишите преобразование в одну строку.
"""

text = 'четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа'


def dict_chr_ord(texts: str) -> dict[str:int]:
    return {item: ord(item) for item in texts}


print(dict_chr_ord(text), '\n')

"""
Задание №3
✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили. Сохраните его итераторатор.
✔ Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.
"""


def from_str_to_dict_2(text_2: str) -> dict[str:int]:
    res_iter = iter({k: ord(k) for k in text_2}.items())
    print(next(res_iter))
    print(next(res_iter))
    print(next(res_iter))
    print(next(res_iter))


from_str_to_dict_2('Самостоятельно')
print('\n')
"""
Задание №4
✔ Создайте генератор чётных чисел от нуля до 100.
✔ Из последовательности исключите числа, сумма цифр которых равна 8.
✔ Решение в одну строку.
"""


def gen_num() -> Generator[int, Any, None]:
    return (item for item in range(0, 101, 2) if item // 10 + item % 10 != 8)


for i in gen_num():
    print(i)

print('\n')

"""
Задание №5
✔ Напишите программу, которая выводит на экран числа от 1 до 100.
✔ При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
✔ Вместо чисел, кратных пяти — слово «Buzz».
✔ Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
✔ *Превратите решение в генераторное выражение.
"""


def fizz_buzz() -> None:
    res_list = (item for item in range(1, 101))
    for item in res_list:
        if item % 15 == 0:
            item = 'Fizz'
        elif item % 3 == 0:
            item = 'FizzBuzz'
        elif item % 5 == 0:
            item = 'Buzz'
        print(item)


fizz_buzz()
print('\n')


def fizz_buzz() -> iter:
    return ('FizzBuzz' if num % 3 == 0 and num % 5 == 0
            else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else num for num in range(1, 101))


fizz_buzz()
print('\n')

"""
Задание №6
✔ Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
✔ Таблицу создайте в виде однострочного генератора, где каждый элемент генератора — отдельный пример таблицы умножения.
✔ Для вывода результата используйте «принт» без перехода на новую строку.
"""


def product_table() -> iter:
    LOWER_LIMIT = 2
    UPPER_lIMIT = 10
    COLUMN = 4

    for item in range(LOWER_LIMIT, UPPER_lIMIT, COLUMN):
        for j in range(LOWER_LIMIT, UPPER_lIMIT + 1):
            for k in range(item, item + COLUMN):
                if j == UPPER_lIMIT and k == item + COLUMN - 1:
                    print(f'{k:>} x {j:>2} = {k * j:>2}\n\n', end='')
                elif k == item + COLUMN - 1:
                    print(f'{k:>} x {j:>2} = {k * j:>2}\n', end='')
                else:
                    print(f'{k:>} x {j:>2} = {k * j:>2}\t\t', end='')


product_table()
print('\n')


def mult_table():
    LOWER_LIMIT = 2
    UPPER_lIMIT = 10
    COLUMN = 4
    print(' ', end='')
    print(*(f'{k:>} x {j:>2} = {k * j:>2}\n\n' if j == UPPER_lIMIT and k == item + COLUMN - 1 else
            f'{k:>} x {j:>2} = {k * j:>2}\n' if k == item + COLUMN - 1 else
            f'{k:>} x {j:>2} = {k * j:>2}\t\t'
            for item in range(LOWER_LIMIT, UPPER_lIMIT, COLUMN)
            for j in range(LOWER_LIMIT, UPPER_lIMIT + 1)
            for k in range(item, item + COLUMN)))


mult_table()
print('\n')

"""
Задание №7
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел, начиная с числа 2.
✔ Для проверки числа на простоту используйте правило: «число является простым, если делится нацело только на единицу и 
на себя».
"""


def prime_gen(n: int) -> (iter, int):
    primes_list = []
    current_number = 2
    while len(primes_list) < n:
        is_prime = True
        for num in primes_list:
            if current_number % num == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(current_number)
            yield current_number
        current_number += 1


print(*(prime_gen(5)))
