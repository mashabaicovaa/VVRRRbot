import telebot
import parser

#main variables
TOKEN = ""
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет,я чат-бот клуба виртуальной реальности ')
bot.polling()

@bot.message_handler(commands=['record'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Забронировать игру ')
bot.polling()
