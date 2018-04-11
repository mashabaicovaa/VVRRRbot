from telebot import types

start_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
start_markup_btn1 = types.KeyboardButton('Запустить')
start_markup.add(start_markup_btn1)

source_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
source_markup_btn1 = types.KeyboardButton('Игры')
source_markup_btn2 = types.KeyboardButton('Цены')
source_markup_btn3 = types.KeyboardButton('Где мы?')
source_markup.add(source_markup_btn1, source_markup_btn2, source_markup_btn3)

age_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
age_markup_btn1 =  types.KeyboardButton('Впечатления')
age_markup_btn2 =  types.KeyboardButton('Симуляторы')
age_markup_btn3 =  types.KeyboardButton('Квесты')
age_markup_btn4 =  types.KeyboardButton('Для любого возраста')
age_markup_btn5 =  types.KeyboardButton('Игры для команд до 4-х человек')
age_markup_btn6 =  types.KeyboardButton('Вернуться в каталог игр')
age_markup.add(age_markup_btn1, age_markup_btn2, age_markup_btn3, age_markup_btn4, age_markup_btn5, age_markup_btn6)

game_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
game_markup_btn1 =  types.KeyboardButton('Забронировать игру')
game_markup_btn2 =  types.KeyboardButton('Посмореть цены')
game_markup_btn3 =  types.KeyboardButton('Вернуться в каталог игр')
game_markup.add(game_markup_btn1, game_markup_btn2, game_markup_btn3)
