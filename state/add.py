from aiogram.dispatcher.filters.state import StatesGroup, State


class AddState(StatesGroup):
    add_start = State()
    ru = State()
    uz = State()
