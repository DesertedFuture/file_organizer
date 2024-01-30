# file_organizer.py
import shutil
import os

class FileOrganizer:
    def __init__(self):
        # Any initialization code for the FileOrganizer class
        return

    def rename_and_move_file(self, source_file, destination_folder, new_name, directory_path):
        file_name=os.path.basename(source_file)
        base_name, extension = os.path.splitext(file_name)
        
        print(destination_folder)
        print(directory_path)

        relative_path = os.path.relpath(destination_folder,directory_path) 
        
        my_name = relative_path.replace('/','_')
        my_name = f"{my_name}_{new_name}{extension}"

        dest_file = os.path.join(destination_folder,my_name)

        try:
            shutil.move(source_file,dest_file)
        except Exception as e:
            print(e)

    #from a button, i want to create a tree
