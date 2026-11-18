import os


dir = str(input("Please enter your target dir: "))

try:
    with os.scandir(dir) as entries:
        dir_names = [entry.name for entry in entries if entry.is_dir()]

        for name in dir_names:
            print(name)

except Exception as e:
    print(f"Error encountered {e}")