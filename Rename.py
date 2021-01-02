# Rename Images with Date Photo Taken

# Import libraries
import os
import sys
from PIL import Image
import shutil

# Set list of valid file extensions
valid_extensions = [".jpg", ".jpeg", ".png", ".JPG"]


# If folder path argument exists then use it
# Else use the current running folder
if len(sys.argv) > 1:
    folder_path = input_file_path = sys.argv[1]

else:
    folder_path = os.getcwd()

# Get folder named
print("Path fo files: ", folder_path)
folder_name = os.path.basename(folder_path.rstrip('/'))
print("Prefix: ", folder_name)

# Convert folder_name to usable filename prefix
# i.e. rmove whtiespaces, umlauts etc

# Get all files from folder with valid_extensions
file_names = os.listdir(folder_path)

# For each file
for file_name in file_names:

    # Get the file extension
    file_ext = os.path.splitext(file_name)[1]

    # If the file does not have a valid file extension
    # then skip it
    if (file_ext not in valid_extensions):
        continue

    # Create the old file path
    old_file_path = os.path.join(folder_path, file_name)

    # Open the image
    image = Image.open(old_file_path)

    # Get the date taken from EXIF metadata
    date_taken = image._getexif()[36867]

    # Close the image
    image.close()

    # Reformat the date taken to "YYYYMMDD-HHmmss"
    date_time = date_taken \
        .replace(":", "")      \
        .replace(" ", "_")

    # Combine the new file name and file extension
    new_file_name = folder_name.replace(" ", "_") + '_' + date_time + file_ext

    # Create the new folder path
    new_file_path = os.path.join(folder_path, new_file_name)

    # Rename the file
    os.rename(old_file_path, new_file_path)

    # Copy and renmae file
    #shutil.copy(old_file_path, new_file_path)
    print(old_file_path)
    print(new_file_path)

# List result

os.system("ls -ltrh " + folder_path)
