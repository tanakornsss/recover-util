import os

def get_dir() -> list:
    root_dir = str(input("Please enter your target directory: "))

    try:
        with os.scandir(root_dir) as entries:
            sub_dir_path = [entry.path for entry in entries if entry.is_dir()]
            return sub_dir_path

    except Exception as e:
        print(f"Error encountered: {e}")
        exit()