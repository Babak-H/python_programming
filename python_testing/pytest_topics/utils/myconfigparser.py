import configparser
from pathlib import Path


class ConfigFileParser:
    cfg_file = 'qa.ini'  # default config file
    cfg_file_directory = 'config'  # default config directory
    config = configparser.ConfigParser()

    def __init__(self, cfg=cfg_file):
        self.cfg_file = cfg  # update the config file if user gives different file name
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.CONFIG_FILE = self.BASE_DIR.joinpath(self.cfg_file_directory).joinpath(self.cfg_file)
        self.config.read(self.CONFIG_FILE)

    def get_gmail_url(self):
        return self.config['gmail']['url']


    def get_gmail_user(self):
        return self.config['gmail']['user']


    def get_gmail_pass(self):
        return self.config['gmail']['pass']


if __name__ == "__main__":
    config = ConfigFileParser('prod.ini')
    print(config.get_gmail_user())
