import pathlib

import yaml

def get_token():
    config = get_config()
    return config["token"]

def is_channel_authorized(server_id, channel_id):
    config = get_config()
    servers = config.get("servers", [])
    for server in servers:
        if server_id == server["id"]:
            channels = server.get("channels", [])
            for channel in channels:
                if channel_id == channel["id"]:
                    return True
    return False

def get_chance_to_butt():
    config = get_config()
    return config.get("chance_to_butt", 0.5)

def contains_keyword(message):
    return "buttbot" in message.lower()

def get_config():
    CONFIG_PATH = get_application_root() / "config.yaml"
    with open(CONFIG_PATH, "r") as config_file:
        config = yaml.load(config_file)
        return config

def get_application_root():
    return pathlib.Path(__file__).parent