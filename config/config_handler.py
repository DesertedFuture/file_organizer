# config/config_handler.py
import configparser
import os


class ConfigHandler:
    def __init__(self, config_path="config/config.ini"):
        self.config_path = config_path
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)

    def update_project_directory(self, new_directory):
        print(f"Updating project directory to: {new_directory}")
        self.config['Paths']['project_directory'] = new_directory
        with open(self.config_path, 'w') as config_file:
            self.config.write(config_file)
            config_file.flush()
            os.fsync(config_file.fileno())
        self.config.read(self.config_path)

    def load_project_directory(self):
        self.config.read(self.config_path)
        project_dir = self.config['Paths']['project_directory']
        print(f"current prject dir: {project_dir}")
        return project_dir

    def update_current_project_path(self, new_path):
        self.config['Paths']['current_project_path'] = new_path
        with open(self.config_path, 'w') as config_file:
            self.config.write(config_file)

    def load_current_project_path(self):
        return self.config['Paths']['current_project_path']

    def update_template_path(self, new_template_path):
        self.config['Paths']['template_path'] = new_template_path
        with open(self.config_path, 'w') as config_file:
            self.config.write(config_file)

    def load_template_path(self):
        return self.config['Paths']['template_path']
