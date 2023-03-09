import hashlib
import os
from os import abort

from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS
from werobot.contrib.flask import make_view

from wechat.message import robot

app = Flask(__name__)
CORS(app, resources=r'/*')

app.add_url_rule(
    rule='/wechat',
    endpoint='werobot',
    view_func=make_view(robot),
    methods=['GET', 'POST']
)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port='3003',
        debug=False
    )
