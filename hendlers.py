from aiogram import Bot, Dispatcher, types
from aiohttp.helpers import TOKEN
from lists import *
import markups as mp
import random
from asyncio import sleep

TOKEN = '2135841143:AAGQD9cz8zcxsoXuaP_vmA64SE8EdpTSvuo'

bot = Bot(token=TOKEN)

# Диспетчер для бота
dp = Dispatcher(bot)

card_filter = set()
# Функция для вызова игр
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.send_message(
        message.from_user.id, 
        f"Привет {message.from_user.full_name}, это бот для игры правда или действие!\nДля начала выберите режим игры:", 
        reply_markup=mp.game_mod
        )
@dp.message_handler(commands=["games"])
async def games(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.send_message(
        message.from_user.id, 
        f"{message.from_user.full_name}, сыграем в игру?\nВыбери одну из игр:", 
        reply_markup=mp.mini_games
        )


@dp.callback_query_handler(text="mod_funny")
async def funny_mod(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    global mod
    mod = dict(truth=list_funny_truth, dare=list_funny_dare, show_mod="Обычный режим 🧩")
    await bot.send_message(message.from_user.id, f"{mod['show_mod']}\nПравда или Действие?", reply_markup=mp.vers)
    
@dp.callback_query_handler(text="mod_18")
async def hard_mod(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    global mod
    mod = dict(truth=list_18_truth, dare=list_18_dare, show_mod="Режим 🔞")
    await bot.send_message(message.from_user.id, f"{mod['show_mod']}\nПравда или Действие?", reply_markup=mp.vers)

@dp.callback_query_handler(text="truth")
async def if_truth(message: types.Message):
    global mod
    await bot.delete_message(message.from_user.id, message.message.message_id)
    card = mod['truth'][random.randint(0, len(mod['truth'])-1)]
    if card not in card_filter:
        await bot.send_message(message.from_user.id, f"{mod['show_mod']} For Elina\nПравда:\n{card}", reply_markup=mp.vers2)
        card_filter.add(card)
    else:
        await bot.send_message(message.from_user.id, f"{mod['show_mod']}\nПравда:\n{card}\nОбнаружен вопрос который уже был, нажмите еще раз!", reply_markup=mp.vers2)

@dp.callback_query_handler(text="dare")
async def if_dare(message: types.Message):
    global mod
    await bot.delete_message(message.from_user.id, message.message.message_id)
    card = mod['dare'][random.randint(0, len(mod['dare'])-1)]
    if card not in card_filter:
        await bot.send_message(message.from_user.id, f"{mod['show_mod']}\nДействие:\n{card}", reply_markup=mp.vers2)
        card_filter.add(card)
    else:
        await bot.send_message(message.from_user.id, f"{mod['show_mod']}\nДействие:\n{card}\nОбнаружено действие которое уже было, нажмите еще раз!", reply_markup=mp.vers2)
    
@dp.callback_query_handler(text="choose_mod")
async def choose_mod(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(
        message.from_user.id, 
        "Выберите другой режим: ", 
        reply_markup=mp.game_mod
        )

@dp.callback_query_handler(text="new")
async def new(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, f"{mod['show_mod']}\nПравда или Действие?", reply_markup=mp.vers)


# Функция с откликом на игру кости
@dp.callback_query_handler(text="bones")
async def play_bones(mesage: types.Message):
    await bot.delete_message(mesage.from_user.id, mesage.message.message_id)
    await bot.send_message(mesage.from_user.id, f"{mesage.from_user.first_name}   VS   BOT")
    
    await sleep(1)

    await bot.send_message(mesage.from_user.id, 'Кость БОТА')
    bot_data = await bot.send_dice(mesage.from_user.id)
    bot_data = bot_data['dice']['value']
    await sleep(5)
    
    await bot.send_message(mesage.from_user.id, f"Кость {mesage.from_user.first_name}")
    user_data = await bot.send_dice(mesage.from_user.id)
    user_data = user_data['dice']['value']
    await sleep(5)

    if bot_data > user_data:
        await bot.send_message(mesage.from_user.id, 'В следующий раз повезет 😁')
    elif user_data > bot_data:
        await bot.send_message(mesage.from_user.id, 'Ты выиграл 😢')
    else:
        await bot.send_message(mesage.from_user.id, 'Упс ничья 😅')


@dp.callback_query_handler(text="darts")
async def play_darts(mesage: types.Message):
    await bot.delete_message(mesage.from_user.id, mesage.message.message_id)
    await bot.send_message(mesage.from_user.id, f"{mesage.from_user.first_name}   VS   BOT")
    
    await sleep(1)

    await bot.send_message(mesage.from_user.id, 'Бросок БОТА')
    bot_data = await bot.send_dice(mesage.from_user.id, emoji="🎯")
    bot_data = bot_data['dice']['value']
    await sleep(5)
    
    await bot.send_message(mesage.from_user.id, f"Бросок {mesage.from_user.first_name}")
    user_data = await bot.send_dice(mesage.from_user.id, emoji="🎯")
    user_data = user_data['dice']['value']
    await sleep(5)

    if bot_data > user_data:
        await bot.send_message(mesage.from_user.id, 'В следующий раз повезет 😁')
    elif user_data > bot_data:
        await bot.send_message(mesage.from_user.id, 'Ты выиграл 😢')
    else:
        await bot.send_message(mesage.from_user.id, 'Упс ничья 😅')

@dp.callback_query_handler(text="bou")
async def play_bou(mesage: types.Message):
    await bot.delete_message(mesage.from_user.id, mesage.message.message_id)
    await bot.send_message(mesage.from_user.id, f"{mesage.from_user.first_name}   VS   BOT")
    
    await sleep(1)

    await bot.send_message(mesage.from_user.id, 'Бросок БОТА')
    bot_data = await bot.send_dice(mesage.from_user.id, emoji="🎳")
    bot_data = bot_data['dice']['value']
    await sleep(5)
    
    await bot.send_message(mesage.from_user.id, f"Бросок {mesage.from_user.first_name}")
    user_data = await bot.send_dice(mesage.from_user.id, emoji="🎳")
    user_data = user_data['dice']['value']
    await sleep(5)

    if bot_data > user_data:
        await bot.send_message(mesage.from_user.id, 'В следующий раз повезет 😁')
    elif user_data > bot_data:
        await bot.send_message(mesage.from_user.id, 'Ты выиграл 😢')
    else:
        await bot.send_message(mesage.from_user.id, 'Упс ничья 😅')
    
@dp.callback_query_handler(text="basket")
async def play_basket(mesage: types.Message):
    await bot.delete_message(mesage.from_user.id, mesage.message.message_id)
    await bot.send_message(mesage.from_user.id, f"{mesage.from_user.first_name}   VS   BOT")
    
    await sleep(1)

    await bot.send_message(mesage.from_user.id, 'Бросок БОТА')
    bot_data = await bot.send_dice(mesage.from_user.id, emoji="🏀")
    bot_data = bot_data['dice']['value']
       
    await sleep(5)
    
    await bot.send_message(mesage.from_user.id, f"Бросок {mesage.from_user.first_name}")
    user_data = await bot.send_dice(mesage.from_user.id, emoji="🏀")
    user_data = user_data['dice']['value']
    await sleep(5)
    if bot_data < 4 and user_data < 4 or bot_data > 3 and user_data > 3:
        await bot.send_message(mesage.from_user.id, 'Упс ничья 😅')
    elif bot_data > user_data and bot_data > 3:
        await bot.send_message(mesage.from_user.id, 'В следующий раз повезет 😁')
    elif user_data > bot_data and user_data > 3:
        await bot.send_message(mesage.from_user.id, 'Ты выиграл 😢')


@dp.callback_query_handler(text="foot")
async def play_foot(mesage: types.Message):
    await bot.delete_message(mesage.from_user.id, mesage.message.message_id)
    await bot.send_message(mesage.from_user.id, f"{mesage.from_user.first_name}   VS   BOT")
    
    await sleep(1)

    await bot.send_message(mesage.from_user.id, 'Удар БОТА')
    bot_data = await bot.send_dice(mesage.from_user.id, emoji="⚽")
    bot_data = bot_data['dice']['value']
       
    await sleep(5)
    
    await bot.send_message(mesage.from_user.id, f"Удар {mesage.from_user.first_name}")
    user_data = await bot.send_dice(mesage.from_user.id, emoji="⚽")
    user_data = user_data['dice']['value']
    await sleep(5)
    if bot_data < 4 and user_data < 4 or bot_data > 3 and user_data > 3:
        await bot.send_message(mesage.from_user.id, 'Упс ничья 😅')
    elif bot_data > user_data and bot_data > 3:
        await bot.send_message(mesage.from_user.id, 'В следующий раз повезет 😁')
    elif user_data > bot_data and user_data > 3:
        await bot.send_message(mesage.from_user.id, 'Ты выиграл 😢')