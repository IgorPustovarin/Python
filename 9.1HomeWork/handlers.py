from aiogram import types
from loader import dp
import random
total = 150
new_game = False
candiesComp = 0

@dp.message_handler(commands=['start', 'старт'])
async def mes_start(message: types.Message):
    print('Вам пришло сообщение')
    print(message)

@dp.message_handler(text=['help', 'помощь'])#text он ищет просто встречающейся текст без знака / в отличии от commands
async def mes_help(message: types.Message):
    await message.answer(message.from_user.id, 'Чем могу помочь тебе?')#answer возвращает сообщение в телеграмм

@dp.message_handler(commands=['new_game'])
async def mes_game(message: types.Message):
    global new_game
    new_game = True
    await message.answer('ДА НАЧНЕТСЯ ВЕЛИКАЯ ИГРА!!!! За ход можно брать не более 28 конфет!')#answer возвращает сообщение в телеграмм
#/set 200
@dp.message_handler(commands=['set'])
async def mes_help(message: types.Message):
    global total
    global new_game
    count = message.text.split()[1]
    if not new_game:
        if count.isdigit():
            total = int(count)
            await message.answer(f'Конфет теперь будет {count} ')
        else:
            await message.answer(f'{message.from_user.first_name}, напишите цифрами')
    else:
            await message.answer(f'{message.from_user.first_name}, нельзя менять правила во время игры')

@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    global new_game
    global candiesComp
    if new_game:
            if message.text.isdigit() and int(message.text) <=28:
                total -= int(message.text)
                await message.answer(f'{message.from_user.first_name} взял {message.text} конфет. '
                                    f'На столе осталось {total}')
                if total <= 0:
                    await message.answer(f'{message.from_user.first_name} ПОБЕДА!!!!')
                    new_game = False
                    total = 150
                if new_game == True:
                    if total > 40:
                        candiesComp = random.randint(1,28)
                    elif total <=40 and total > 30:
                        candiesComp = random.randint(1,10)
                    elif total <=30 and total > 28:
                        candiesComp = 1
                    elif total <=28:
                        candiesComp = total
                    total -= candiesComp
                    await message.answer(f'Компьютер взял {candiesComp} конфет. '
                                        f'На столе осталось {total}')
                    if total <= 0:
                        await message.answer(f'Победил компьютер')
                        new_game = False
                        total = 150