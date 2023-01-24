from dotenv import load_dotenv
import os
import requests
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler

CHAT_ID = 244065258
TEXT = 'Привет-привет'
URL = 'https://api.thecatapi.com/v1/images/search'

load_dotenv()
token = os.getenv('TOKEN')

updater = Updater(token=token)


def get_new_image():
    try:
        response = requests.get(URL)
    except Exception as e:
        print(e)
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)

    response = response.json()
    random_cat = response[0].get('url')
    return random_cat


def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup([['/newcat']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}, смотри какие котаны!'.format(name),
        reply_markup=buttons,
    )


updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))

updater.start_polling()
updater.idle()
