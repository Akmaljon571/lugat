from aiogram.dispatcher.filters.state import StatesGroup, State


class small_game_state(StatesGroup):
    game = State()
