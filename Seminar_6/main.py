import new_task as nt
import generate as gen
from sys import argv

from Python_next_deep.Seminar_6 import task, date_validate

if __name__ == '__main__':
    _, *arg = argv
    gen.gen_fnc(*(int(i) for i in argv[1:]))
    gen.gen_fnc(10, 20, 5)
    try_count = task.puzzle("Не лает не кусает, в дом не пускает.", ["замок", "замочек", "засов"], 3)
    if try_count:
        print(f"Угадано за {try_count} раза")
    else:
        print("Не угадали (")
    puzzle_dict = {
        "Не лает не кусает, в дом не пускает.": ["замок", "замочек", "засов"],
        "Красна девица, а коса на улице": ["морковь", "морковка"],
        "два кольца, два конца, в середине гвоздик": ["ножницы"],
    }

    nt.new_puzzle(puzzle_dict, 3)
    nt.show_result()

    data = '12.01.1999'
    print(date_validate.date_validator(data))
