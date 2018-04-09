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

@bot.message_handler(commands = ['url'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Наш сайт', url='https://vr.gameofmind.ru/')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup = markup)
