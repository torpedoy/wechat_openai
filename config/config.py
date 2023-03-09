import os

import dotenv
from pathlib import Path
from dotenv import load_dotenv

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load .env config
config_env = dotenv.dotenv_values(config_dir / "config.env")

env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)

print(os.getenv('WECHAT_TOKEN'))
