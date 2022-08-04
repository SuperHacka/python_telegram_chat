from flask import Flask
from flask import request
from flask import Response
import requests

TOKEN = "5582586897:AAE9yeS7A-QVeePacjxXB5CBJq6DwDBK1G0"
app = Flask(__name__)


def parse_message(message):
    print("message-->", message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("chat_id-->", chat_id)
    print("txt-->", txt)
    return chat_id, txt


def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    r = requests.post(url, json=payload)
    return r


def tel_send_video(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendVideo'

    payload = {
        'chat_id': chat_id,
        "video": "https://www.appsloveworld.com/wp-content/uploads/2018/10/640.mp4",

    }

    r = requests.post(url, json=payload)

    return r


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()

        chat_id, txt = parse_message(msg)
        if "hi" in txt:
            tel_send_message(chat_id, "Hello welcome to the telegram bot")
        else:
            tel_send_message(chat_id, "Sorry couldn't quite catch that")

        return Response('System is working', status=200)
    else:
        return "<h1>Welcome!</h1>"


if __name__ == '__main__':
    app.run(debug=True)
