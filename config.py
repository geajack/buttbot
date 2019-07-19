import pathlib

import yaml

def get_token():
    config = get_config()
    return config["token"]

def get_config():
    CONFIG_PATH = get_application_root() / "config.yaml"
    with open(CONFIG_PATH, "r") as config_file:
        config = yaml.load(config_file)
        return config

def get_application_root():
    return pathlib.Path(__file__).parent