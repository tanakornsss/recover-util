from pathlib import Path
from src.utils import get_dir

to_remove_paths = []

# Folder level iter
for path in get_dir():
    dir_path = Path(path)

    # File iter
    for file in dir_path.glob("t*.jpg"):
        to_remove_paths.append(file)

# Write file list to remove
with open("to_remove.txt", "w", newline="", encoding="utf-8") as f:
    for path in to_remove_paths:
        f.write(f"{str(path)}\n")

# Ask for confirmation
confirmation = str(input("Are you sure? Type 'yes' (case sensitive) to confirm: "))
if confirmation == "yes":
    for path in to_remove_paths:
        current = Path(path)

        print(f"Removing: {current}")
        current.unlink(missing_ok=True)

    print("Done!")
