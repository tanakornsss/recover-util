import os

from pathlib import Path

# Ask user for a root dir
root_dir = str(input("Please enter your target directory: "))
sub_dir_path = []

try:
    with os.scandir(root_dir) as entries:
        sub_dir_path = [entry.path for entry in entries if entry.is_dir()]

except Exception as e:
    print(f"Error encountered: {e}")
    exit()

to_remove_paths = []

# Folder level iter
for path in sub_dir_path:
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
