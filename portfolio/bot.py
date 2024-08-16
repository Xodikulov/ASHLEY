import requests
from environs import Env

env = Env()
env.read_env()

def send_message(text):
    BOT_TOKEN = env.str("BOT_TOKEN")
    CHAT_ID = env.str("CHAT_ID")
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': text}
    response = requests.post(url, data=payload)
    
    print(response.json())  # Yuborilgan javobni chiqarish

# Misol uchun chaqirish
send_message('Hello, this is a message.')
