"""
Main run
"""
import os
from pathlib import Path

from DZ_1 import group_rename
from DZ_3 import make_files
from DZ_7 import two_files_in_one
from DZ_8 import feel_numbers
from DZ_9 import name_gen

if __name__ == "__main__":
    print(__name__)
    print(os.listdir())
    feel_numbers(5, 'nums')
    name_gen(10, 4, 7, Path('name_gen'))
    two_files_in_one(Path('nums'), Path('name_gen'), Path('result'))
    make_files('bin', count=2)
    group_rename(4, 'bin', 'zip', [2, 4], "new")