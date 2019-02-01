import variables as var
import requests  

upd = var.methods['updates']
send = var.methods['send']

def get_updates(bot_token):
    res = requests.get(var.tel_api_url.format(bot_token)+upd)
    return res.json()
    pass


def get_chat_id(bot_token):
	return get_updates(bot_token)['result'][-1]['message']['chat']['id']



def get_last_message(json_answer):
    text_answer = json_answer['result'][-1]['message']['text']
    return text_answer
    pass


def send_message(text_message):
	chat_id = get_chat_id(var.bot_token)
	text = text_message
	params = {'chat_id':chat_id,'text':text_message}
	requests.post(var.tel_api_url.format(var.bot_token)+send, params)


def echo_mess():
    last_mess_text = get_last_message(get_updates(var.bot_token))
    while True:
        send_message(last_mess_text)


if __name__ == '__main__':  
    try:
        echo_mess()
    except KeyboardInterrupt:
        exit()        

