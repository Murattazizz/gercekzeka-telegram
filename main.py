import requests

TOKEN = 7881163080:AAGsHk7MYWkqTktPFv_JM7aInTKWK32ffpc
CHAT_ID = 6544723713

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=data)

def gercekzeka_gorevi():
    mesaj = "GerçekZeka sistemi otomatik görevini tamamladı."
    send_telegram_message(mesaj)

if __name__ == "__main__":
    gercekzeka_gorevi()
