#!/usr/bin/env python

import os
import shutil

# downloads_folder = "Downloads"
downloads_folder = "C:\\Users\\thede\\Downloads"
total_files_moved = 0

# Get list of files in the Downloads folder
files = os.listdir(downloads_folder)

# Iterate through each file
for file_name in files:
    file_path = os.path.join(downloads_folder, file_name)

    # Check if it's a file and not a directory
    if os.path.isfile(file_path):
        # Extract file extension
        file_extension = os.path.splitext(file_name)[1]

        # Remove the dot from the extension
        file_extension = file_extension[1:]

        # Create folder if it doesn't exist
        folder_path = os.path.join(downloads_folder, file_extension)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created new directory: {file_extension}")

        # Move the file to the folder with matching extension
        shutil.move(file_path, os.path.join(folder_path, file_name))
        total_files_moved += 1

print(f"Total number of files moved: {total_files_moved}")
