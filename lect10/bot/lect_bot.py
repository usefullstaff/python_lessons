import requests  

bot_token = '724789546:AAGKGVe2C3opt27HOaXbw_KBvOlCAbZ9Tfg'
tel_api_url = "https://api.telegram.org/bot{}/"

methods = {'updates': 'GetUpdates',
		   'send': 'sendMessage'}

class MyBot:
	upd = methods['updates']
	send = methods['send']
	tel_api_url = tel_api_url

	def __init__(self, bot_token = None, ):
		self.token = bot_token

	def get_updates(self):
		res = requests.get(self.tel_api_url.format(self.token)+self.upd)
		return res.json()
		pass	

	def get_chat_id(self):
		res =  self.get_updates()['result'][-1]['message']['chat']['id']
		return res
		pass

	
	def get_last_message(self):
		text_answer = self.get_updates()['result'][-1]['message']['text']
		return text_answer
		pass


	def send_message(self,text_message = 'Default message'):
		chat_id = self.get_chat_id()
		text = text_message
		params = {'chat_id':chat_id,'text':text_message}
		requests.post(self.tel_api_url.format(self.token)+self.send, params)	

	def echo_mess(self):
		last_mess_text = self.get_last_message()
		self.send_message(last_mess_text)


bot = MyBot(bot_token)

