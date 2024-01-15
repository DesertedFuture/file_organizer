# config_handler.py
import configparser
import os

class ConfigHandler:
    def __init__(self, config_file_path='config.ini'):
        self.config_file_path = config_file_path
        self.config = configparser.ConfigParser()

        # Load existing configuration
        self.load_configuration()

    def load_configuration(self):
        if os.path.exists(self.config_file_path):
            self.config.read(self.config_file_path)
        else:
            # Set default values if the configuration file doesn't exist
            self.create_default_configuration()

    def create_default_configuration(self):
        # Set default values for configuration options
        self.config['Directories'] = {
            'ConstantDirectory': '',
            'SourceFolder': '',
            'SpecDirectory': ''
        }

        # Save the default configuration to the file
        with open(self.config_file_path, 'w') as configfile:
            self.config.write(configfile)

    def get_constant_directory(self):
        return self.config.get('Directories', 'ConstantDirectory', fallback='')

    def set_constant_directory(self, path):
        self.config.set('Directories', 'ConstantDirectory', path)
        with open(self.config_file_path, 'w') as configfile:
            self.config.write(configfile)
