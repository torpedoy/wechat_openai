from werobot import WeRoBot
from werobot.replies import WeChatReply, TextReply, ImageReply

robot = WeRoBot(
    token="ddd"
)


@robot.subscribe
def subscribe(message):
    return "你好，欢迎关注"


@robot.text
def text(message):
    return "xxx"
