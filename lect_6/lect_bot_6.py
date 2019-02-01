import variables_class as var
import requests  


class MyBot:
	upd = var.methods['updates']
	send = var.methods['send']
	tel_api_url = var.telegram_api_url

	def __init__(self, bot_token = None, ):
		self.token = bot_token

	def get_updates(self):
		res = requests.get(self.tel_api_url.format(self.token)+self.upd)
		return res.json()
		pass	

	def get_chat_id(self):
		return self.get_updates()['result'][-1]['message']['chat']['id']
		pass

	
	def get_last_message(self):
		text_answer = self.get_updates()['result'][-1]['message']['text']
		return text_answer
		pass


	def send_message(self, text_message = 'Default message'):
		chat_id = self.get_chat_id()
		text = text_message
		params = {'chat_id':chat_id,'text':text_message}
		requests.post(self.tel_api_url.format(self.token)+self.send, params)
		print(requests.post(self.tel_api_url.format(self.token)+self.send, params))	

	def echo_mess(self):
		last_mess_text = self.get_last_message()
		self.send_message(last_mess_text)


print(MyBot(var.bot_token).get_chat_id())
#print(MyBot(var.bot_token).get_updates())
#print(MyBot(var.bot_token).get_last_message())
#MyBot(var.bot_token).echo_mess()
MyBot(var.bot_token).send_message()
#MyBot(var.bot_token).send_message('work!')