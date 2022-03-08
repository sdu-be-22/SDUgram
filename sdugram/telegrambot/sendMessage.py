import requests
import telebot
import os

from .models import TeleSettings



def sendTelegram(tg_name, tg_phone, tg_img):
	settings = TeleSettings.objects.get(pk=1)
	token = str(settings.tg_token)
	chat_id = str(settings.tg_chat)
	text = str(settings.tg_message)
	api = 'https://api.telegram.org/bot'
	method = api + token + '/sendMessage'
	bot = telebot.TeleBot(token)
	a = text.find('{')
	b = text.find('}')
	c = text.rfind('{')
	d = text.rfind('}')

	part_1 = text[0:a]
	part_2 = text[b+1:c]
	part_3 = text[d:-1]

	text_slise = part_1 + tg_name + part_2 + str(tg_phone) + part_3
	# e = tg_img.find('1_')
	# tg_img = tg_img[e+2:len(tg_img)]
	# print(tg_img)
	dire = os.getcwd().replace('\\', '/')
	img = open(dire + '/' + str(tg_img.url), 'rb')
	bot.send_photo(chat_id, img)
	req = requests.post(method, data={
		'chat_id': chat_id,
		'text': text_slise
		})
