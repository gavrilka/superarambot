# -*- coding: utf-8 -*-
import os
import telebot
import requests
import time
import random

TOKEN = "495756900:AAGvm2io0-UCK4nopKkLCuPgLXXMqV3H2Xs"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)
# add handlers
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://superarambot2.herokuapp.com/" + TOKEN)
updater.idle()

@bot.message_handler(commands=['help'])
def helpCommand(message):
    bot.send_message(message.chat.id, 'Привет *' + message.from_user.first_name + '*!', parse_mode='Markdown')
