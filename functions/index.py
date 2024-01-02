from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from random import randint

from api.index import API
from keyboard.button import start_button, game
from keyboard.inline import remove_inline
from setting import ADMIN, bot
from state.add import AddState
from state.big_game import big_game_state
from state.small_game import small_game_state
from state.translate import Translate
from database.connect import *


async def start_fn(message: types.Message):
    chat_id = message.from_user.id
    if chat_id == ADMIN:
        await bot.send_photo(chat_id,
                             photo='AgACAgIAAxkBAAMGZZO2acY1TaRu-k61MBa2IpePEd8AAk_PMRvrMaFIT1tKYweIKTUBAAMCAAN5AAM0BA',
                             caption='Здравствуйте, мы продолжаем запоминать слово ?',
                             reply_markup=start_button())


async def translate_fn(message: types.Message):
    await Translate.translate_start.set()
    await message.answer('Tarjima qilingan so`zni kiriting: ', reply_markup=ReplyKeyboardRemove())


async def translate_step_fn(message: types.Message, state: FSMContext):
    text = API(message.text)['responseData']['translatedText']
    await state.finish()
    await message.answer(text)


async def add_fn(message: types.Message):
    await AddState.add_start.set()
    await message.answer('Введите новое слово 🇷🇺', reply_markup=ReplyKeyboardRemove())


async def add_ru_fn(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ru'] = message.text
    await AddState.ru.set()
    await message.answer('Введите новое слово 🇺🇿')


async def add_uz_fn(message: types.Message, state: FSMContext):
    data = await state.get_data()
    ru = data.get('ru')
    create(uz=message.text, ru=ru)
    await state.finish()
    await message.answer('Добавлено новое слово', reply_markup=start_button())


async def remove_fn(message: types.message):
    await message.answer('Выберите слово для удаления', reply_markup=remove_inline())


async def callback_fn(call: types.CallbackQuery):
    data = call.data
    if data.startswith('prev'):
        step = int(data.split('=')[-1]) - 10
        await bot.edit_message_text(chat_id=ADMIN,
                                    text="Updated Inline Keyboard",
                                    message_id=call.message.message_id,
                                    reply_markup=remove_inline(step))
    elif data.startswith('next'):
        step = int(data.split('=')[-1]) + 10
        await bot.edit_message_text(chat_id=ADMIN,
                                    text="Updated Inline Keyboard",
                                    message_id=call.message.message_id,
                                    reply_markup=remove_inline(step))
    else:
        delete(data)
        await call.message.answer('Boldi ochirildi')


async def big_game_fn(message: types.Message, state):
    data = get_all()
    random = randint(0, len(data))
    await big_game_state.game.set()
    async with state.proxy() as baza:
        baza['id'] = data[random]['id']
    await message.answer(data[random]['ru'], reply_markup=game())


async def big_result_fn(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data_id = data.get('id')
    one = get_one(id=data_id)
    await message.answer(one['uz'])


async def big_next_fn(message: types.Message, state: FSMContext):
    data = get_all()
    random = randint(0, len(data))
    async with state.proxy() as baza:
        baza['id'] = data[random]['id']
    await message.answer(data[random]['ru'], reply_markup=game())


async def big_finish_fn(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Игра окончена', reply_markup=start_button())


async def small_game_fn(message: types.Message, state):
    data = get_last_10()
    random = randint(0, len(data))
    await small_game_state.game.set()
    async with state.proxy() as baza:
        baza['id'] = data[random]['id']
    await message.answer(data[random]['ru'], reply_markup=game())


async def small_result_fn(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data_id = data.get('id')
    one = get_one(id=data_id)
    await message.answer(one['uz'])


async def small_next_fn(message: types.Message, state: FSMContext):
    data = get_last_10()
    random = randint(0, len(data))
    async with state.proxy() as baza:
        baza['id'] = data[random]['id']
    await message.answer(data[random]['ru'], reply_markup=game())


async def small_finish_fn(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Игра окончена', reply_markup=start_button())
