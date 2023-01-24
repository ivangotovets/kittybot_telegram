import requests
from telegram import Bot

TOKEN = '5829159779:AAHdFKHv34HKT3f1UwnUR0xlhY0U3jRZstE'
CHAT_ID = 244065258
TEXT = 'Привет-привет'
URL = 'https://api.thecatapi.com/v1/images/search'

bot = Bot(token=TOKEN)
response = requests.get(URL).json()
pict_url = response[0].get('url')


bot.send_message(CHAT_ID, TEXT)
bot.send_photo(CHAT_ID, pict_url)
