import os
from dotenv import load_dotenv
import yaml

load_dotenv()

class Config:
    def __init__(self):
        with open('config/config.yaml', 'r') as f:
            self.config = yaml.safe_load(f)

    def get(self, key, default=None):
        return os.getenv(key) or self.config.get(key, default)

config = Config()