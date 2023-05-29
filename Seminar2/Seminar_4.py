"""Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
Строки нумеруются начиная с единицы
Слова выводятся отсортированными согласно кодировки Unicode
Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки

22:04
Напишите функцию, которая принимает строку текста.
Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию"""



def task6():
     input_data = input("Enter your data: ")
     words_list = input_data.split()
     max_length = len(words_list[0])
     for i in words_list:
         if len(i) > max_length:
             max_length = len(i)

     words_list.sort()
     for num_line, line in enumerate(words_list, start=1):
         print(f"{num_line} {line:>{max_length}}")
