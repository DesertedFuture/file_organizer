# organizer/file_organizer.py
import os
import shutil
from config.config_handler import ConfigHandler


class FileOrganizer:
    def __init__(self):
        # Create a ConfigHandler instance to load configuration settings
        self.config_handler = ConfigHandler()

    def move_and_rename_file(self,
                             source_file_path,
                             destination_folder,
                             rename_text):
        try:
            # Ensure the destination folder exists
            os.makedirs(destination_folder, exist_ok=True)

            # Move and rename the file
            new_file_path = os.path.join(destination_folder, rename_text)
            shutil.move(source_file_path, new_file_path)

            return True, new_file_path  # Success
        except Exception as e:
            return False, str(e)  # Failure

    def create_new_project(self, project_name):
        try:
            project_directory = self.config_handler.load_project_directory()
            os.makedirs(project_directory, exist_ok=True)
            template_path = self.config_handler.load_template_path()
            new_project_path = os.path.join(project_directory, project_name)

            os.makedirs(new_project_path)
            shutil.copytree(
                    template_path,
                    new_project_path,
                    dirs_exist_ok=True)

            return True, f"Project '{project_name}' created successfully."
        except Exception as e:
            return False, str(e)
