# config/config_handler.py
import configparser


class ConfigHandler:
    def __init__(self, config_path="config/config.ini"):
        self.config_path = config_path
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)

    def update_project_directory(self, new_directory):
        self.config['Paths']['project_directory'] = new_directory
        with open(self.config_path, 'w') as config_file:
            self.config.write(config_file)

    def load_project_directory(self):
        return self.config['Paths']['project_directory']

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
