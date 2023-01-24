from telegram import Bot

bot = Bot(token='5829159779:AAHdFKHv34HKT3f1UwnUR0xlhY0U3jRZstE')
chat_id = '244065258'
text = 'Вам телеграмма!'
bot.send_message(chat_id, text)