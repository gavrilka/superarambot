# -*- coding: utf-8 -*-
import telebot
import requests
import time
import os
import random

from yobit import get_btc
from yobit import get_money
from telebot import types
from flask import Flask, request
from flask_sslify import SSLify
token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token, threaded=False)

bot.remove_webhook()
time.sleep(1)
bot.set_webhook(url='https://superarambot.herokuapp.com' + '/' + token)

app = Flask(__name__)
sslify = SSLify(app)


@app.route('/')
def base():
    return 'bot'


@app.route('/' + token, methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "ok", 200


@bot.message_handler(commands=['help'])
def helpCommand(message):
    bot.send_message(message.chat.id, 'Привет *' + message.from_user.first_name + '*!', parse_mode='Markdown')

@bot.message_handler(commands=['money'])
def moneyCommand(message):
    try:
        text = message.text
        texts = text.split(' ')
        bot.send_message(message.chat.id, 'Привет *' + message.from_user.first_name + '*, на текущий момент курс ' + '*' + texts[1] + ' *' + 'составляет: ' + '*' + get_money(texts[2], texts[1]) + '*', parse_mode='Markdown')
    except Exception as e:
        logger.error(e.message)

if __name__ == '__main__':
    app.run()
