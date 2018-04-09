import telebot
from Task import Task
import parser
import markups as m

#main variables
TOKEN = "540973546:AAHkrTMvWclty8NSkCsQ1Bc5WqIiOUgvEUw"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['record'])
def record_handler(message):
    bot.send_message(message.chat.id, 'Забронировать игру ')

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    if not task.isRunning:
        chat_id = message.chat.id
        msg = bot.send_message(chat_id, 'Привет, я чат-бот клуба виртуальной реальности. Пожалуйста, выбери внизу из предложенных вариантов что ты хочешь посмотреть', reply_markup=m.source_markup)
        bot.register_next_step_handler(msg, askSource)
        task.isRunning = True

bot.polling(none_stop=True)

