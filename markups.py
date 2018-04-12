from telebot import types

start_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
start_markup_btn1 = types.KeyboardButton('Запустить')
start_markup.add(start_markup_btn1)

menu_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
menu_markup_btn1 = types.KeyboardButton('Игры')
menu_markup_btn2 = types.KeyboardButton('Цены')
menu_markup_btn3 = types.KeyboardButton('Где мы?')
menu_markup.add(menu_markup_btn1, menu_markup_btn2, menu_markup_btn3)

catalog_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
catalog_markup_btn1 =  types.KeyboardButton('Впечатления')
catalog_markup_btn2 =  types.KeyboardButton('Симуляторы')
catalog_markup_btn3 =  types.KeyboardButton('Квесты')
catalog_markup_btn4 =  types.KeyboardButton('Для любого возраста')
catalog_markup_btn5 =  types.KeyboardButton('Игры для команд до 4-х человек')
catalog_markup_btn6 =  types.KeyboardButton('Вернуться в главное меню')
catalog_markup.add(catalog_markup_btn1, catalog_markup_btn2, catalog_markup_btn3, catalog_markup_btn4, catalog_markup_btn5, catalog_markup_btn6)

game_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
game_markup_btn1 =  types.KeyboardButton('Забронировать время')
game_markup_btn2 =  types.KeyboardButton('Посмотреть цены')
game_markup_btn3 =  types.KeyboardButton('Вернуться в каталог игр')
game_markup.add(game_markup_btn1, game_markup_btn2, game_markup_btn3)
