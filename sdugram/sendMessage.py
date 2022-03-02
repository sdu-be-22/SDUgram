import requests
import telebot

token = '5252466115:AAFtzD_zayfwcTeKu2ovArUjobWqlTB1Pr4'
chat_id = '@zayavki_f'
text = 'Test_1'
bot = telebot.TeleBot(token)

def sendTelegram():
	api = 'https://api.telegram.org/bot'
	method = api + token + '/sendMessage'
	img = open('2.jpg', 'rb')
	bot.send_photo(chat_id, img)
	req = requests.post(method, data={
		'chat_id': chat_id,
		'text': text
		})

sendTelegram()