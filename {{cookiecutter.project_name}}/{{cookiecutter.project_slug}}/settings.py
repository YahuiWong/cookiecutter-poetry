from typing import Dict, List

import yaml


class Settings:
    _config: Dict

    @classmethod
    def init(cls, file_path: str):
        with open(file_path, "r") as f:
            cls._config = yaml.safe_load(f)

    @classmethod
    def debug(cls):
        return cls.get("core", "debug")

    @classmethod
    def monitoring(cls):
        return cls.get("core", "monitoring")
    @classmethod

    def get(cls, *args):
        """
        get config item
        """
        c = cls._config
        for arg in args:
            c = c.get(arg)
        return c