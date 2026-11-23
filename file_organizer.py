import os
import shutil

folder_path = input("Enter folder path: ")

# Check that the folder exists
if not os.path.isdir(folder_path):
    print("Error: Please enter a valid folder path.")

else:
    for filename in os.listdir(folder_path):

        # Skip hidden files such as .DS_Store
        if filename.startswith("."):
            continue

        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):

            if "." not in filename:
                continue

            ext = filename.split(".")[-1]
            new_folder = os.path.join(folder_path, ext)

            if not os.path.exists(new_folder):
                os.makedirs(new_folder)

            destination = os.path.join(new_folder, filename)

            # Don't overwrite files that already exist
            if os.path.exists(destination):
                print("Skipped: " + filename + " already exists.")

            else:
                shutil.move(file_path, destination)
                print("Moved: " + filename)

    print("Finished organizing files!")
