import os
import shutil
source = input("Enter the name of source folder")
destination = input("Enter the name of destination folder")
source = source+"/"
destination = destination+"/"
list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.move(source+file,destination)