import configparser
import os

CONFIG_PATH = "settings.ini"


def create_config_if_not_exists():
    if not os.path.exists(CONFIG_PATH):
        config = configparser.ConfigParser()
        config.add_section("Settings")
        config.set("Settings", "FileFormat", "scv")  
        config.set("Settings", "FileName", "phonebook.pickle")  
        with open(CONFIG_PATH, "w") as config_file:
            config.write(config_file)
 
def update_config():
    file_format = input("")
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)    
    config.set("Settings", "FileFormat", file_format)
    config.set("Settings", "FileName", 'phonebook.'+file_format)
    with open(CONFIG_PATH, "w") as config_file:
        config.write(config_file)

def read_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    file_format = config.get("Settings", "FileFormat")
    return file_format

def read_config_file_name():
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    file_name = config.get("Settings", "FileName")
    return file_name
