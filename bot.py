import telebot
from Task import Task
import markups as m
from game import game

#main variables
TOKEN = "540973546:AAHkrTMvWclty8NSkCsQ1Bc5WqIiOUgvEUw"
bot = telebot.TeleBot(TOKEN)
task = Task()

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
        task.mySource = 'игры'
        msg = bot.send_message(chat_id, 'Выберите категорию игр', reply_markup=m.age_markup)
        bot.register_next_step_handler(msg, askAge)
    elif text in task.names[1]:
        task.mySource = 'цена'
        msg = bot.send_message(chat_id, 'Стоимость игр', reply_markup=m.rating_markup)
        bot.register_next_step_handler(msg, askRating)
    else:
        msg = bot.send_message(chat_id, 'Бронирование и адрес')
        return

def askAge(message):
    chat_id = message.chat.id
    text = message.text.lower()
    filters = task.filters
    if text not in filters:
        msg = bot.send_message(chat_id, 'Такой категории нет.Пожалуйста выберите другую категорию')
        bot.register_next_step_handler(msg, askAge)
        return
    elif text == task.filters[0]:
    #task.myFilter = task.filters_code_names[0][filters.index(text)]
        msg = bot.send_message(chat_id, game.game1())
        bot.register_next_step_handler(msg, askAmount)

def askAmount(message):
    chat_id = message.chat.id
    task.isRunning = False
    
bot.polling(none_stop=True)

