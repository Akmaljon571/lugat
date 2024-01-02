from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from database.connect import get_all


def remove_inline(step=0):
    stop = step + 10
    lugat_all = get_all()[step:stop]
    inline = InlineKeyboardMarkup(row_width=2)
    arr = []
    for i, a in enumerate(lugat_all):
        arr.append(InlineKeyboardButton(text=a['uz'], callback_data=a['id']))
    if step != 0:
        arr.append(InlineKeyboardButton(text='Prev', callback_data=f'prev={step}'))
    if len(get_all()) > stop:
        arr.append(InlineKeyboardButton(text="Next", callback_data=f'next={step}'))
    inline.add(*arr)
    return inline
