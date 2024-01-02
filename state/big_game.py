from aiogram.dispatcher.filters.state import StatesGroup, State


class big_game_state(StatesGroup):
    game = State()
