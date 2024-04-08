import requests


API_URL = 'https://api.telegram.org/bot'BOT_TOKEN = '7004016973:AAFuptvSJsZ_NQpoHaQMW64Mnd_L1IzuxhA'
TEXT1 = 'текст'
TEXT2 = 'фото'
TEXT3 = 'видео'
TEXT4 = 'стикер'
MAX_COUNTER = 100
offset = -2
counter = 0
chat_id: int


while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:        
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            typemessage = result['message']]
    if typemessage['text']:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT1}')            
    elif typemessage['photo']:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT2}')            
    elif typemessage['video']:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT3}')            
    elif typemessage['sticker']:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT4}')
    time.sleep(1)
    counter += 1
