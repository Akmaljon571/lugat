from setting import dp
from functions.index import *


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await start_fn(message)


@dp.message_handler(text='Перевести ♻️')
async def translate(message: types.Message):
    await translate_fn(message)


@dp.message_handler(state=Translate.translate_start)
async def translate_step(message: types.Message, state: FSMContext):
    await translate_step_fn(message, state)


@dp.message_handler(text='Добавление словаря ✍️')
async def add(message: types.Message):
    await add_fn(message)


@dp.message_handler(state=AddState.add_start)
async def translate_step1(message: types.Message, state: FSMContext):
    await add_ru_fn(message, state)


@dp.message_handler(state=AddState.ru)
async def translate_step2(message: types.Message, state: FSMContext):
    await add_uz_fn(message, state)


@dp.message_handler(text='Удаление словаря 🗑')
async def translate_step2(message: types.Message):
    await remove_fn(message)


@dp.message_handler(text='Большая игра 🎲')
async def big_game(message: types.Message, state: FSMContext):
    await big_game_fn(message, state)


@dp.message_handler(text='Pезультат 🤔', state=big_game_state.game)
async def big_result(message: types.Message, state: FSMContext):
    await big_result_fn(message, state)


@dp.message_handler(text='Cледующий ⏭', state=big_game_state.game)
async def big_next(message: types.Message, state: FSMContext):
    await big_next_fn(message, state)


@dp.message_handler(text='Заканчивать 🏁', state=big_game_state.game)
async def big_finish(message: types.Message, state: FSMContext):
    await big_finish_fn(message, state)


@dp.message_handler(text='Mаленький игра 10x 🎮')
async def small_game(message: types.Message, state: FSMContext):
    await small_game_fn(message, state)


@dp.message_handler(text='Pезультат 🤔', state=small_game_state.game)
async def small_result(message: types.Message, state: FSMContext):
    await small_result_fn(message, state)


@dp.message_handler(text='Cледующий ⏭', state=small_game_state.game)
async def small_next(message: types.Message, state: FSMContext):
    await small_next_fn(message, state)


@dp.message_handler(text='Заканчивать 🏁', state=small_game_state.game)
async def small_finish(message: types.Message, state: FSMContext):
    await small_finish_fn(message, state)


@dp.callback_query_handler()
async def callback(call: types.CallbackQuery):
    await callback_fn(call)


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def photo(message: types.Message):
    photo_file_id = message.photo[-1].file_id
    print(photo_file_id)
