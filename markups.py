from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

game_mod = InlineKeyboardMarkup(row_width=2)
mod_18 = InlineKeyboardButton(text="Режим для двоих 🔞", callback_data="mod_18")
mod_funny = InlineKeyboardButton(text="Обычный режим 🧩", callback_data="mod_funny")

game_mod.insert(mod_18)
game_mod.insert(mod_funny)

vers = InlineKeyboardMarkup(row_width=2)
vers2 = InlineKeyboardMarkup(row_width=2)

truth = InlineKeyboardButton(text="Правда 🗣", callback_data="truth")
dare = InlineKeyboardButton(text="Действие 👀", callback_data="dare")
choose_mod = InlineKeyboardButton(text="Выбор режима ↩️", callback_data="choose_mod")
new = InlineKeyboardButton(text="Далее ✅", callback_data="new")

vers.add(truth).add(dare).add(choose_mod)
vers2.add(choose_mod).insert(new)

mini_games = InlineKeyboardMarkup(row_width=2)
bones = InlineKeyboardButton(text="Кости🎲", callback_data="bones")
darts = InlineKeyboardButton(text="Дартс🎯", callback_data="darts")
bou = InlineKeyboardButton(text="Боулинг🎳", callback_data="bou")
basket = InlineKeyboardButton(text="Баскетбол🏀", callback_data="basket")
foot = InlineKeyboardButton(text="Футбол⚽", callback_data="foot")
mini_games.add(bones).add(darts).add(bou).add(basket).add(foot)