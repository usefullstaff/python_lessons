import variables as var
import requests  

class MyBot:
	upd = var.methods['updates']
	send = var.methods['send']
	tel_api_url = var.telegram_api_url

	def __init__(self, bot_token = None, ):
		self.token = bot_token

	def get_updates(self):
    	res = requests.get(tel_api_url.format(self.token)+upd)
    	return res.json()
    	pass	

    def get_chat_id(bot_token):
		return self.get_updates()['result'][-1]['message']['chat']['id']
		pass

	
	def get_last_message(json_answer):
    	text_answer = json_answer['result'][-1]['message']['text']
    	return text_answer
    	pass


    def send_message(text_message = 'Default message'):
		chat_id = self.get_chat_id(token)
		text = text_message
		params = {'chat_id':chat_id,'text':text_message}
		requests.post(tel_api_url.format(token)+send, params)	

	def echo_mess(self):
		last_mess_text = self.get_last_message(self.get_updates(token))
		self.send_message(last_mess_text)
