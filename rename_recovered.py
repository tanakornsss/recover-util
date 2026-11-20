import os

from src.utils import get_dir


file_list = []

for path in get_dir():
    file_list.extend(
        os.path.join(path, f)
        for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f))
    )

for file in file_list:
    print(file)
