import requests

token = '5252466115:AAFtzD_zayfwcTeKu2ovArUjobWqlTB1Pr4'
chat_id = '@zayavki_f'
text = 'Test_1'

def sendTelegram():
	api = 'https://api.telegram.org/bot'
	method = api + token + '/sendMessage'

	req = requests.post(method, data={
		'chat_id': chat_id,
		'text': text
		})

sendTelegram()