from ..errors import ConfigError
import json
from .comments import strip_comments


def load_config(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            config = f.read()
            clean_config = strip_comments(config)
            config_json = json.loads(clean_config)
    except (OSError, json.JSONDecodeError, UnicodeDecodeError) as e:
        raise ConfigError(f"Opening file failed: {e}")

    print(config_json)


load_config("/home/mzougari/Desktop/Pac-Man/config.json")