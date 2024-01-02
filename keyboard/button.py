from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_button():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [
        KeyboardButton('Большая игра 🎲'),
        KeyboardButton('Mаленький игра 10x 🎮'),
        KeyboardButton('Добавление словаря ✍️'),
        KeyboardButton('Удаление словаря 🗑'),
        KeyboardButton('Перевести ♻️'),
    ]
    keyboard.add(*buttons)
    return keyboard


def game():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [
        KeyboardButton('Pезультат 🤔'),
        KeyboardButton('Cледующий ⏭'),
        KeyboardButton('Заканчивать 🏁'),
    ]
    keyboard.add(*buttons)
    return keyboard
