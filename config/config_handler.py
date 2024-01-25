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
        required_options = {'Settings:' ['project_directory']}

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

    def load_config(self):

