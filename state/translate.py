from aiogram.dispatcher.filters.state import StatesGroup, State


class Translate(StatesGroup):
    translate_start = State()
