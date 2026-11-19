import os

# Ask user for a root dir
root_dir = str(input("Please enter your target dir: "))
sub_dir_path = []

try:
    with os.scandir(root_dir) as entries:
        sub_dir_path = [entry.path for entry in entries if entry.is_dir()]

except Exception as e:
    print(f"Error encountered {e}")
    exit()

files_path = []

for path in sub_dir_path:
    files_path.extend(
        os.path.join(path, f)
        for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f))
    )

# Print findings report
with open("debug.txt", "w", newline="", encoding="utf-8") as file:
    for path in files_path:
        file.write(f"{path}\n")
