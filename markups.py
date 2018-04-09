from telebot import types

start_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
start_markup_btn1 = types.KeyboardButton('/start')
start_markup.add(start_markup_btn1)

source_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
source_markup_btn1 = types.KeyboardButton('Забронировать игру')
source_markup_btn2 = types.KeyboardButton('Цены')
source_markup_btn3 = types.KeyboardButton('Где мы?')
source_markup.add(source_markup_btn1, source_markup_btn2, source_markup_btn3)

age_markup = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
age_markup_btn1 =  types.KeyboardButton('Один')
age_markup_btn2 =  types.KeyboardButton('Два')
age_markup_btn3 =  types.KeyboardButton('Три')
age_markup_btn4 =  types.KeyboardButton('Четыре')
age_markup.add(age_markup_btn1, age_markup_btn2, age_markup_btn3, age_markup_btn4)
