import os

# Ask user for a root dir
root_dir = str(input("Please enter your target dir: "))
sub_dir_path = []

try:
    with os.scandir(root_dir) as entries:
        sub_dir_path = [entry.path for entry in entries if entry.is_dir()]

except Exception as e:
    print(f"Error encountered {e}")

for path in sub_dir_path:
    print(path)