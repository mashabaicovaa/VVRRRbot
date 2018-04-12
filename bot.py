import telebot
from Task import Task
import markups as m
from game import game
from price import price

#main variables
TOKEN = "540973546:AAHkrTMvWclty8NSkCsQ1Bc5WqIiOUgvEUw"
bot = telebot.TeleBot(TOKEN)
task = Task()

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    if not task.isRunning:
        chat_id = message.chat.id
        msg = bot.send_message(chat_id, 'Привет, я чат-бот клуба виртуальной реальности. Пожалуйста, выбери внизу из предложенных вариантов что ты хочешь посмотреть', reply_markup=m.menu_markup)
        bot.register_next_step_handler(msg, main_menu)
        task.isRunning = True
        
def main_menu(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if text in task.names[0]:
        msg = bot.send_message(chat_id, 'Выберите категорию игр', reply_markup=m.catalog_markup)
        bot.register_next_step_handler(msg, game_catalog)
    elif text in task.names[1]:
        msg = bot.send_message(chat_id, price.all_price, reply_markup=m.back_markup)
        bot.register_next_step_handler(msg, askA)
    else:
        msg = bot.send_message(chat_id, 'Где мы находимся ?')
        return

def game_catalog(message):
    chat_id = message.chat.id
    text = message.text.lower()
    filters = task.filters
    if text not in filters:
        msg = bot.send_message(chat_id, 'Такой категории нет.Пожалуйста выберите другую категорию')
        bot.register_next_step_handler(msg, game_catalog)
        return
    elif text == task.filters[0]:
        gamesCount=len(game.game1)
        if not gamesCount==0:
            for i in range(0,gamesCount):
                if not i==gamesCount-1:
                     bot.send_message(chat_id, game.game1[i], reply_markup=m.game_markup)
                else:
                     msg = bot.send_message(chat_id, game.game1[i], reply_markup=m.game_markup)
                     
                     bot.register_next_step_handler(msg, game_menu)
    elif text == task.filters[1]:
        gamesCount=len(game.game1)
        if not gamesCount==0:
            for i in range(0,gamesCount):
                if not i==gamesCount-1:
                     bot.send_message(chat_id, game.game2[i], reply_markup=m.game_markup)
                else:
                     msg = bot.send_message(chat_id, game.game2[i], reply_markup=m.game_markup)
                     
                     bot.register_next_step_handler(msg, game_menu)
    elif text == task.filters[2]:
        gamesCount=len(game.game1)
        if not gamesCount==0:
            for i in range(0,gamesCount):
                if not i==gamesCount-1:
                     bot.send_message(chat_id, game.game3[i], reply_markup=m.game_markup)
                else:
                     msg = bot.send_message(chat_id, game.game3[i], reply_markup=m.game_markup)
                     
                     bot.register_next_step_handler(msg, game_menu)
    elif text == task.filters[3]:
        gamesCount=len(game.game1)
        if not gamesCount==0:
            for i in range(0,gamesCount):
                if not i==gamesCount-1:
                     bot.send_message(chat_id, game.game4[i], reply_markup=m.game_markup)
                else:
                     msg = bot.send_message(chat_id, game.game4[i], reply_markup=m.game_markup)
                     
                     bot.register_next_step_handler(msg, game_menu)
    elif text == task.filters[4]:
        gamesCount=len(game.game1)
        if not gamesCount==0:
            for i in range(0,gamesCount):
                if not i==gamesCount-1:
                     bot.send_message(chat_id, game.game5[i], reply_markup=m.game_markup)
                else:
                     msg = bot.send_message(chat_id, game.game5[i], reply_markup=m.game_markup)
                     
                     bot.register_next_step_handler(msg, game_menu)
    elif text == task.filters[5]:
        msg = bot.send_message(chat_id, 'Пожалуйста, выбери из представленных внизу вариантов, чтоты хочешь посмотреть', reply_markup=m.menu_markup)
        bot.register_next_step_handler(msg, main_menu)


def game_menu(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if text in task.names[3]:
        msg = bot.send_message(chat_id, 'Давайте забронируем время')
        bot.register_next_step_handler(msg, askA)
    elif text in task.names[1]:
        msg = bot.send_message(chat_id, 'Прайс на цены', reply_markup=m.rating_markup)
        bot.register_next_step_handler(msg, askRating)
    elif text in task.names[0]:
        msg = bot.send_message(chat_id, 'Выберите категорию игр', reply_markup=m.catalog_markup)
        bot.register_next_step_handler(msg, game_catalog)
    else:
        msg = bot.send_message(chat_id, 'Я Вас не понял. Выберите, пожалуйста, еще раз.')
        bot.register_next_step_handler(msg, game_menu)
        return

def price(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if text in task.price[0]:
        msg = bot.send_message(chat_id, price.price, reply_markup=m.menu_markup)
        bot.register_next_step_handler(msg, main_menu)
    else:
        msg = bot.send_message(chat_id, 'Я Вас не понимаю, пожалуйста ыернитесь в главное меню.')
        return

def askA(message):
    chat_id = message.chat.id
    text = message.text.lower()
    bot.send_message(chat_id, 'Бот завершил работу')
    task.isRunning = False
    
bot.polling(none_stop=True)

