import os

from werobot import WeRoBot
from openai_bot import api

robot = WeRoBot(
    token = os.getenv('WECHAT_TOKEN')
)
robot.config["APP_ID"] = os.getenv('WECHAT_APP_ID')
robot.config["APP_SECRET"] = os.getenv('WECHAT_APP_SECRET')
robot.config["ENCODING_AES_KEY"] = os.getenv('WECHAT_ENCODING_AES_KEY')

@robot.subscribe
def subscribe(message):
    return "你好，欢迎关注"

@robot.text
def text(message):
    openid = message.FromUserName
    msg = message.content
    new_messages = _generate_messages(msg, openid, "user")
    replay = api.completion_turbo(new_messages)
    replay_save = _generate_messages(replay, openid)
    return replay


def _generate_messages(message, openid, chat_mode="system"):
    new_message_data = {"role":chat_mode,"content":message}
    messages = []
    messages.append(new_message_data)

    return messages