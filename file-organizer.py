import os
import shutil

def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            ext = file.split(".")[-1].lower() if "." in file else "no_extension"
            target_dir = os.path.join(folder_path, ext)

            os.makedirs(target_dir, exist_ok=True)
            shutil.move(full_path, os.path.join(target_dir, file))

    print("Folder organized successfully!")

if __name__ == "__main__":
    path = input("Enter folder path: ")
    organize_folder(path)
