import telebot
import parser

#main variables
TOKEN = "540973546:AAHkrTMvWclty8NSkCsQ1Bc5WqIiOUgvEUw"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['record'])
def record_handler(message):
    bot.send_message(message.chat.id, 'Забронировать игру ')

@bot.message_handler(commands=['start')
def start_handler(message):
    chat_id = message.chat.id
    text = message.text
    msg = bot.send_message(chat_id, 'Привет, я чат-бот виртуальной реальности./n Нажми 1 если хочешь забронировать игру или нажми для просмотра цен и другой информации')
    bot.register_next_step_handler(msg, askAge)

def askAge(message):
    chat_id = message.chat.id
    text = message.text
    if  text.isdigit():
        msg = bot.send_message(chat_id, 'Возраст должен быть числом, введите ещё раз.')
        bot.register_next_step_handler(msg, askAge) #askSource
        return
    msg = bot.send_message(chat_id, 'Спасибо, я запомнил что вам ' + text + ' лет.')

    

bot.polling(none_stop=True)

