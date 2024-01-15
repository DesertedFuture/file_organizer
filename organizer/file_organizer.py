# file_organizer.py
import os
import shutil

class FileOrganizer:
    def __init__(self, config_handler):
        self.config_handler = config_handler

    def organize_files(self):
        constant_directory = self.config_handler.get_constant_directory()

        # Ensure the constant directory is set
        if not constant_directory:
            print("Constant directory not set. Please configure it in the settings.")
            return

        # Perform file organization logic
        # ...

    def move_and_rename_files(self, source_folder, spec_file_path):
        # Your logic for moving and renaming files based on the specification file
        # ...
        if not constant_directory:
            print("Constant directory not set. Please configure it in the settings.")
            return

    def create_folders_from_spec(self, constant_directory, spec_file_path):
        # Your logic for creating folders based on the specification file
        # ...
        if not constant_directory:
            print("Constant directory not set. Please configure it in the settings.")
            return

    def run(self):
        # Your main logic for organizing files
        self.organize_files()
