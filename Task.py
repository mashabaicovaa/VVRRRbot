class Task():
    isRunning = False
    names = [
        ['игры', 'игру', 'игра', 'каталог', 'посмотреть', 'вернуться в каталог игр' ],
        ['цена', 'цену', 'топ', 'цены'],
        ['адрес', 'находитесь', 'all'],
        ['забронировать', 'бронь', 'забронировать время']
        
    ]
    menu = [
        ['вернуться в главное меню', 'меню']
        ]
    
    filters = ['впечатления',
               'симуляторы',
               'квесты',
               'для любого возраста',
               'игры для команд до 4-х человек',
               'вернуться в главное меню']
    
    filters_code_names = [
        ['daily', 'weekly', 'monthly'],
        ['all', 'top10', 'top25', 'top50', 'top100']
    ]
    price = [
        ['посмотреть цены','цена', 'цену', 'цены']
        ]
    all_price = [
        ['20 минут -300 р\n40 минут-500р\n60 минут- 700р']
        ]
    
    mySource = ''
    myFilter = ''
    def __init__(self):
        return
