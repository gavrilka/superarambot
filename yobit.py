# -*- coding: utf-8 -*-
import requests

def get_money(pair, base): #курс бата к доллару, рублю
    url1 = 'https://api.fixer.io/latest?base=' + base
    response = requests.get(url1).json()
    price = response['rates'][pair]
    return str(price)

def get_btc(): #курс биткоина к доллару
    url1 = 'https://yobit.net/api/2/btc_usd/ticker'
    response = requests.get(url1).json()
    price = response['ticker']['last']
    return str(price) + ' usd'