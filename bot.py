import telebot
import parser
import markups as m

#main variables
TOKEN = "540973546:AAHkrTMvWclty8NSkCsQ1Bc5WqIiOUgvEUw"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['record'])
def record_handler(message):
    bot.send_message(message.chat.id, 'Забронировать игру ')

#@bot.message_handler(commands=['start'])
#def start_handler(message):
   #bot.send_message(message.chat.id, 'Привет,я чат-бот клуба виртуальной реальности ')

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
        chat_id = message.chat.id
        msg = bot.send_message(chat_id, 'Откуда парсить?', reply_markup=m.source_markup)
        bot.register_next_step_handler(msg, askSource)

bot.polling(none_stop=True)

