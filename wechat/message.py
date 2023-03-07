import hashlib
from os import abort

from flask import request
from werobot import WeRoBot
from werobot.replies import WeChatReply, TextReply, ImageReply

robot = WeRoBot(
    token="dddd"
)
robot.config["APP_ID"] = "$$$$$$"               # 写入开发者ID
robot.config["ENCODING_AES_KEY"] = "$$$$$$"

@robot.subscribe
def subscribe(message):
    return "你好，欢迎关注"

@robot.text
def text(message):
    openid = message.FromUserName

    return "生成中。。。"
