import telebot
from Task import Task
import markups as m

#main variables
TOKEN = "540973546:AAHkrTMvWclty8NSkCsQ1Bc5WqIiOUgvEUw"
bot = telebot.TeleBot(TOKEN)
task = Task()

#@bot.message_handler(commands=['record'])
#def record_handler(message):
   # bot.send_message(message.chat.id, 'Забронировать игру ')

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    if not task.isRunning:
        chat_id = message.chat.id
        msg = bot.send_message(chat_id, 'Привет, я чат-бот клуба виртуальной реальности. Пожалуйста, выбери внизу из предложенных вариантов что ты хочешь посмотреть', reply_markup=m.source_markup)
        bot.register_next_step_handler(msg, askSource)
        task.isRunning = True
        
def askSource(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if text in task.names[0]:
        task.mySource = 'игра'
        msg = bot.send_message(chat_id, 'Выберите категорию игр', reply_markup=m.age_markup)
        bot.register_next_step_handler(msg, askAge)
    elif text in task.names[1]:
        task.mySource = 'цена'
        msg = bot.send_message(chat_id, 'Сколько стоит игра?', reply_markup=m.rating_markup)
        bot.register_next_step_handler(msg, askRating)
    else:
        msg = bot.send_message(chat_id, 'Мы находимся тут.')
        bot.register_next_step_handler(msg, askSource)
        return

bot.polling(none_stop=True)

