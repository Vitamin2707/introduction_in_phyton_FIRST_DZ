from pathlib import Path

from csv_to_json import csv_to_json
from next_functions import gen_csv_with_nums, quadratic_equation
from deco_param import fact
from multy import multy
from two_numbers import two_numbers
from two_numbers_two import two_numbers_two

if __name__ == '__main__':
    csv_to_json(Path('file_out.csv'), Path('json_in.json'))
    print(fact(5))
    results = two_numbers(3, 20)
    print(results)
    results()
    two_numbers_two(11, 20)
    multy(6, 7, temp=2, res=3, c=2, d=5)
    print(fact(5))
    gen_csv_with_nums()
    quadratic_equation()
