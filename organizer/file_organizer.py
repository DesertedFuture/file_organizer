# file_organizer.py
import shutil
import os

class FileOrganizer:
    def __init__(self):
        # Any initialization code for the FileOrganizer class
        return

    def rename_and_move_file(self, source_file, destination_folder, new_name):
        # Extract the base name and extension from the source file
        base_name, extension = os.path.splitext(os.path.basename(source_file))
        print(base_name)

        # Construct the new file name with the desired architecture
        new_file_name = f"{base_name}_{new_name}{extension}"
        print(new_file_name)

        # Construct the full path for the destination file
        destination_file = os.path.join(destination_folder, new_file_name)

        # Move the file to the new location with the new name
        shutil.move(source_file, destination_file)
        print(source_file)
        print(destination_file)
        print(new_file_name)


    # Add other methods related to file organization here
