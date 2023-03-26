from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

uir_1_button = InlineKeyboardButton(text="УИР-1", callback_data="uir-1")
poks_1_button = InlineKeyboardButton(text="ПОКС-1", callback_data="poks-1")
fiz_1_button = InlineKeyboardButton(text="ФИЗ-1", callback_data="fiz-1")
mi_1_button = InlineKeyboardButton(text="МИ-1", callback_data="mi-1")
web_1_button = InlineKeyboardButton(text="ВЕБ-1", callback_data="web-1")
pm_1_button = InlineKeyboardButton(text="ПМ-1", callback_data="pm-1")
poit_1_button = InlineKeyboardButton(text="ПОИТ-1", callback_data="poit-1")
isit_1_button = InlineKeyboardButton(text="ИСИТ-1", callback_data="isit-1")

uir_2_button = InlineKeyboardButton(text="УИР-2", callback_data="uir-2")
poks_2_button = InlineKeyboardButton(text="ПОКС-2", callback_data="poks-2")
fiz_2_button = InlineKeyboardButton(text="ФИЗ-2", callback_data="fiz-2")
mi_2_button = InlineKeyboardButton(text="МИ-2", callback_data="mi-2")
web_2_button = InlineKeyboardButton(text="ВЕБ-2", callback_data="web-2")
pm_2_button = InlineKeyboardButton(text="ПМ-2", callback_data="pm-2")
poit_2_button = InlineKeyboardButton(text="ПОИТ-2", callback_data="poit-2")
isit_2_button = InlineKeyboardButton(text="ИСИТ-2", callback_data="isit-2")

group_keyboard = InlineKeyboardMarkup(row_width=2).add(uir_1_button, uir_2_button, poks_1_button, poks_2_button, fiz_1_button, fiz_2_button,
                                                       mi_1_button, mi_2_button, web_1_button, web_2_button, pm_1_button, pm_2_button, poit_1_button, poit_2_button, isit_1_button, isit_2_button)

  
