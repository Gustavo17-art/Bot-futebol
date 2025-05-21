import time
import requests

token = '7856695773:AAGsRuisEf1KZ_pnq9ub7YBhEEpzpunFCZQ'
chat_id = '1187078721'

def enviar_telegram(mensagem):
    url_req = f'https://api.telegram.org/bot{token}/sendMessage'
    params = {'chat_id': chat_id, 'text': mensagem}
    requests.get(url_req, params=params)

while True:
    enviar_telegram('Bot funcionando!')
    time.sleep(600)  # envia mensagem a cada 10 minutos
