#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from telegram.ext import Updater, CommandHandler

updater = Updater(token = '726392781:AAGXBRGIwud9J_9Bu0oxEdcpvmfouDJ6As4')
dispatcher = updater.dispatcher

dades = {}
num = random.randint(1,100)

def hello(bot, update):
    resposta = 'Eyo wassup'
    bot.send_message(chat_id = update.message.chat_id, text = resposta)

def imatge(bot, update):
	imatge = './hellocat.png'
	bot.send_photo(chat_id = update.message.chat_id, photo = open(imatge, 'rb'))

def guess(bot, update, args):
	
	global num
	userid = update.message.from_user['id']

	if userid not in dades:
		
		x = 0
		numJugador = int(args[0])
		dades[userid] = {'numJug': numJugador, 'intents': x, 'secret': num}
				
	resposta = "Has triat el número " + str(args[0])
	bot.send_message(chat_id = update.message.chat_id, text = resposta)

	numJugador = int(args[0])
	dades[userid].update({'numJug': numJugador})
		
	print("numero a endevinar: ", dades[userid]['secret'])
	
	if numJugador < num:
			
		resposta = "Fred fred això està fred"
		bot.send_message(chat_id = update.message.chat_id, text = resposta)
			
	elif numJugador > num:
			
		resposta = "Onde vaaaaaaas!"
		bot.send_message(chat_id = update.message.chat_id, text = resposta)

	elif numJugador == num:
			
		del dades[userid]
		num = random.randint(1,100)		
		resposta = "Esa eeeees maquina"
		bot.send_message(chat_id = update.message.chat_id, text = resposta)
		print (" ========= JOC NOU =========")

handlers = [CommandHandler('hello', hello),
            CommandHandler('imatge', imatge), 
            CommandHandler('guess', guess, pass_args = True)]

for handler in handlers:
    dispatcher.add_handler(handler)

updater.start_polling()
