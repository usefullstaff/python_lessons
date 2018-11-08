import variables as var
import requests  

upd = var.methods['updates']
send = var.methods['send']

def get_updates(bot_token, method):
    res = requests.get(var.tel_api_url.format(bot_token)+method)
    return res.json()
    pass


def get_message_text(json_answer):
    text_answer = json_answer['result'][-1]['message']['text']
    chat_id = json_answer['result'][-1]['message']['chat']['id']
    return text_answer, chat_id
    pass
    

def send_message():
	chat_id = get_message_text(get_updates(var.bot_token, upd))[1]
	requests.post(var.tel_api_url.format(var.bot_token)+send, {'chat_id':chat_id,'text':'text'} )

send_message()
print(get_message_text(get_updates(var.bot_token, upd)))