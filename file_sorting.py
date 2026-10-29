import os
import shutil

folder = "files"

for file in os.listdir(folder):

    file_path = os.path.join(folder, file)

    if os.path.isfile(file_path):


        extension = os.path.splitext(file)[1].lower()


        extension = extension[1:]

        if extension == "":
            folder_name = "Others"
        else:
            folder_name = extension.upper()


        destination = os.path.join(folder, folder_name)

        if not os.path.exists(destination):
            os.mkdir(destination)

        shutil.move(file_path, destination)

print("Files arranged successfully!")