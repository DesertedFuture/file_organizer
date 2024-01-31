# config_handler.py
import configparser
import os
import shutil

class ConfigHandler:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_file = 'config/config.ini'

        if not os.path.exists('config/config.ini') or not self.validate_config_structure():
            self.create_default_config()

    def validate_config_structure(self):
        required_sections=['Settings']
        required_options = {'Settings': ['project_directory', 'template']}

        try:
            self.config.read(self.config_file)

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
            self.config['Settings'] = {'project_directory': '', 'template': ''}

            with open('config/config.ini', 'w') as configfile:
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
            print("error getting {setting}")
            return None

    
    def save_config(self):
        with open('config/config.ini', 'w') as configfile:
            self.config.write(configfile)
   

    def load_directory(self):
        return self.load_setting('project_directory')
   
    #
    # projects directory
    #
    def update_d(self, folder):
        print(folder)
        self.config.set('Settings', 'project_directory', str(folder))
        self.save_config()

    #
    # project template
    #

    def update_template(self, folder):
        self.config.set('Settings', 'template', str(folder))
        self.save_config()

    def get_project_template(self):
        return self.config.get('Settings','template')

    def set_project_template(self, template):
        tempate_str = ','.join(template)
        self.config.set('Settings','template', template_str)
        self.save_config()
