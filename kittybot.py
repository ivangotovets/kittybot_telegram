from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler

updater = Updater(token='5829159779:AAHdFKHv34HKT3f1UwnUR0xlhY0U3jRZstE')


def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Привет, я KittyBot!')


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(
        chat_id=chat.id,
        text='Спасибо, что включил, {}'.format(name)
    )


updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

updater.start_polling(poll_interval=20.0)
updater.idle()
