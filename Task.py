class Task():
    isRunning = False
    names = [
        ['игры', 'игру', 'игра', 'каталог', 'посмотреть', 'вернуться в каталог игр' ],
        ['цена', 'цену', 'топ', 'цены', 'посмотреть цены'],
        ['адрес', 'находитесь', 'all'],
        ['забронировать', 'бронь', 'забронировать время'],
        ['где мы?', 'где мы', 'адрес']
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
        ['показать цены','цена', 'цену', 'цены']
        ]
    all_price = ['20 минут -300 р\n40 минут-500р\n60 минут- 700р']
        
    adress = ['Мы находимся по адрему там то тамто . Связаться с нами можно по телефону ....']
    
    mySource = ''
    myFilter = ''
    def __init__(self):
        return
