import os
import shutil

path = input("Enter the path of the folder: ").strip()  # Remove leading/trailing spaces
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]  # Remove the dot from the extension
    
    if extension:  # Only proceed if there is an extension
        if os.path.exists(os.path.join(path, extension)):
            shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
        else:
            os.makedirs(os.path.join(path, extension))
            shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
