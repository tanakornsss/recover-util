import os

from datetime import datetime
from pathlib import Path
from src.utils import get_dir

file_list = []

for path in get_dir():
    file_list.extend(
        os.path.join(path, f)
        for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f))
    )

repeated_name_cnt = 0
confirmation = str(input("Are you sure? Type 'yes' (case sensitive) to confirm: "))
if confirmation == "yes":
    for file in file_list:
        file_path = Path(file)

        stats = file_path.stat()
        m_date_time = datetime.fromtimestamp(stats.st_mtime)
        formatted = m_date_time.strftime("%Y-%m-%d_%H-%M-%S")

        print(f"Processing: {file_path}")

        new_path = file_path.with_stem(formatted)

        repeated_name_cnt = 0
        while new_path.exists():
            repeated_name_cnt += 1
            new_path = file_path.with_stem(
                f"{formatted}({repeated_name_cnt})"
            )

        file_path.rename(new_path)

    print("Done!")

