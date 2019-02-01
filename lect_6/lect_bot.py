import requests  

first_name = 'jensen'
bot_name = 'E42Bot'


bot_token = '724789546:AAGKGVe2C3opt27HOaXbw_KBvOlCAbZ9Tfg'
tel_api_url = "https://api.telegram.org/bot{}/"

methods = {'updates': 'GetUpdates'}



def get_updates():
    res = requests.get(tel_api_url.format(bot_token)+methods['updates'])
    return res.json()



def get_message_text(json_answer):
    text_answer = json_answer['result'][-1]['message']['text']
    chat_id = json_answer['result'][-1]['message']['chat']['id']
    return text_answer, chat_id
    pass

print(get_message_text(get_updates()))
