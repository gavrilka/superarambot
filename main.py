# -*- coding: utf-8 -*-
import telebot
import requests
import time
import os

from flask import Flask, request

token = os.environ['TELEGRAM_TOKEN']

bot = telebot.TeleBot(token, threaded=False)

server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

@server.route('/' + token, methods=["POST"])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://superarambot2.herokuapp.com' + '/' + token)
    return "!", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
server = Flask(__name__)
