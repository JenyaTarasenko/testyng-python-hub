import requests
from django.conf import settings

def  send_telegram_message(contact):
    TELEGRAM_BOT_TOKEN = settings.TELEGRAM_BOT_TOKEN
    TELEGRAM_CHAT_ID = settings.TELEGRAM_CHAT_ID
    
    
    massage = (
        f"Новое сообщение от:{contact.name}\nНомер телефона:{contact.number},\nКомменрарий :{contact.comment}"
    )
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": massage}
    
    response = requests.post(url, data=data)
    if response.status_code != 200:
        print(f"Ошибка отправки в Telegram: {response.text}")
        
        
        