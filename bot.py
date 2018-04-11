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
        #task.mySource = 'игры'
        msg = bot.send_message(chat_id, 'Выберите категорию игр', reply_markup=m.age_markup)
        bot.register_next_step_handler(msg, askAge)
    elif text in task.names[1]:
        #task.mySource = 'цена'
        msg = bot.send_message(chat_id, 'Цены', reply_markup=m.rating_markup)
        bot.register_next_step_handler(msg, askRating)
    else:
        msg = bot.send_message(chat_id, 'Где мы находимся ?')
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
        #msg = bot.send_message(chat_id, game.game1 )
        gamesCount=len(game.game1)
        if not gamesCount==0:
            for i in range(0,gamesCount):
                if not i==gamesCount-1:
                     bot.send_message(chat_id, game.game1[i], reply_markup=m.game_markup)
                else:
                     msg = bot.send_message(chat_id, game.game1[i], reply_markup=m.game_markup)
                     
                     bot.register_next_step_handler(msg, askAmount)



def askAmount(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if text in task.names[3]:
        task.mySource = 'забронировать'
        msg = bot.send_message(chat_id, 'Давайте забронируем время', reply_markup=m.age_markup)
        bot.register_next_step_handler(msg, askA)
    elif text in task.names[1]:
        #task.mySource = 'цены'
        msg = bot.send_message(chat_id, 'Прайс на цены', reply_markup=m.rating_markup)
        bot.register_next_step_handler(msg, askRating)
    elif text in task.names[0]:
        msg = bot.send_message(chat_id, 'Выберите категорию игр', reply_markup=m.age_markup)
        bot.register_next_step_handler(msg, askAge)
    else:
        msg = bot.send_message(chat_id, 'Я Вас не понял. Выберите, пожалуйста, еще раз.')
        bot.register_next_step_handler(msg, askAmount)
        return

def askA(message):
    chat_id = message.chat.id
    text = message.text.lower()
    bot.send_message(chat_id, 'Бот завершил работу')
    task.isRunning = False
    
bot.polling(none_stop=True)

