# config_handler.py
import configparser
import os

class ConfigHandler:
    def __init__(self):
        self.config = configparser.ConfigParser()

        if not os.path.exists('config.ini') or not self.validate_config_structure():
            self.create_default_config()

    def validate_config_structure(self):
        required_sections=['Settings']
        required_options = {'Settings': ['project_directory']}

        try:
            self.config.read('config.ini')

            for section in required_sections:
                if not self.config.has_section(section):
                    return False
            for option in required_options.get(section,[]):
                if not self.config.has_option(section, option):
                    return False
        except configparser.Error:
            return False

        return True
    
    def create_default_config(self):
    # Create or overwrite the config file with default values
        try:
            self.config['Settings'] = {'project_directory': ''}

            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)

        except configparser.Error as e:
            # Handle the case when there is an error while creating the config file
            print(f"Error creating default configuration: {e}")

    def load_setting(self, setting):
        if not self.config.sections():
            self.load_config()

        try:
            project_d = self.config.get('Settings', setting)
            return project_d
        except (configparser.Error, configparser.NoOptionError, configparser.NoSectionError):
            print("error getting project_directory")
            return None
    def load_directory(self):
        return self.load_setting('project_directory')
    
    def update_d(self, folder):
        print(folder)
        self.config.set('Settings', 'project_directory', str(folder))
        self.save_config()
    def save_config(self):
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

