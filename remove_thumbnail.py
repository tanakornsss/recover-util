import os

# Ask user for a root dir
root_dir = str(input("Please enter your target dir: "))
sub_dir_path = []

try:
    with os.scandir(root_dir) as entries:
        sub_dir_path = [f"{root_dir}\\" + entry.name for entry in entries if entry.is_dir()]

except Exception as e:
    print(f"Error encountered {e}")

for sub_path in sub_dir_path:
    print(sub_path)