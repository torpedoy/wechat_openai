import os
from flask import session

from werobot import WeRoBot

from config import config
from openai_bot import api

robot = WeRoBot(
    token = config.WECHAT_TOKEN
)
robot.config["APP_ID"] = config.WECHAT_APP_ID
robot.config["APP_SECRET"] = config.WECHAT_APP_SECRET
robot.config["ENCODING_AES_KEY"] = config.WECHAT_ENCODING_AES_KEY

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
    # 异步队列处理消息
    _save_messages(replay_save)
    return "思考中，请稍后..."



def _generate_messages(message, openid, chat_mode="system"):
    new_message_data = {"role":chat_mode,"content":message}
    #存进session
    messages = session.get(openid, [])
    messages.append(new_message_data)
    session[openid] = messages
    return messages

def _save_messages(messages):
    # 异步队列处理消息
    pass