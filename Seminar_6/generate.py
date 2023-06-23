import random as rnd


def gen_fnc(low: int = 1, height: int = 50, try_count: int = 5) -> bool:
    result = False
    num = rnd.randint(low, height + 1)

    search_count = 0
    while search_count < try_count:
        ask_value = int(input(f"Введите число от {low} до {height}: "))
        if ask_value == num:
            print("Вы угадали")
            result = True
            break
        if ask_value < num:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")
        search_count += 1
    else:
        print("Попытки закончились")

    return result