from flask import Flask
from flask_cors import CORS
from werobot.contrib.flask import make_view

from wechat import message

app = Flask(__name__)
CORS(app, resources=r'/*')

app.add_url_rule(
    rule='/wechat',
    endpoint='werobot',
    view_func=make_view(message),
    methods=['GET', 'POST']
)


@app.route("/", methods=['GET', 'POST'])
def base():
    return "hello"


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port='3003',
        debug=False
    )
