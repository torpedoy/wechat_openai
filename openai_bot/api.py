import os
import openai

from config import config

openai.api_key = os.getenv('OPENAI_API_KEY')

def completion_turbo(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    replay = response["choices"][0]["message"]["content"]
    return replay