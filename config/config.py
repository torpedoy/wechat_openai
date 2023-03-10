import dotenv
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load .env config
config_env = dotenv.dotenv_values(config_dir / "config.env")

# config parameters
WECHAT_TOKEN = config_env["WECHAT_TOKEN"]
WECHAT_APP_ID = config_env["WECHAT_APP_ID"]
WECHAT_APP_SECRET = config_env["WECHAT_APP_SECRET"]
WECHAT_ENCODING_AES_KEY = config_env["WECHAT_ENCODING_AES_KEY"]
OPENAI_API_KEY = config_env["OPENAI_API_KEY"]
