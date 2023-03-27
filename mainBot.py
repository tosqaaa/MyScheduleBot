from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import logging
import asyncio
from db import Subscriber
from datetime import datetime
from aiogram.utils import executor
from db import ScheduleData
from Exceler import end_week_day, get_xlsx_name
from keys import BOT_TOKEN, DAYS, DAYS_RU
from messages import *
from keyboards import *


logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN, parse_mode="html")
dp = Dispatcher(bot=bot)
db = Subscriber()


sch_data = ScheduleData(to_update=True)

@dp.callback_query_handler(text="uir-1")  # Колбэк на УИР
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.answer(text="Специальность: УИР")
    await bot.send_message(callback_query.from_user.id, text=SELECTED_UIR)
    for i in range(1, 7):
        await bot.send_message(callback_query.from_user.id, text=f"<b><i>{end_week_day}</i></b>\n \n♦️<i><b><u>{DAYS_RU[6-i]}</u></b></i>♦️\n" + sch_data.getDataFromDB(group_id="13_1", day=DAYS[6-i]))
        await bot.send_message(callback_query.from_user.id, text="⭐️⭐️⭐️⭐️⭐️⭐️")


@dp.callback_query_handler(text="poks-1")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.answer(text="Специальность: ПОКС")
    await bot.send_message(callback_query.from_user.id, text=SELECTED_POKS)
    for i in range(1, 7):
        # 11_1
        await bot.send_message(callback_query.from_user.id, text=f"<b><i>{end_week_day}</i></b>\n \n♦️<i><b><u>{DAYS_RU[6-i]}</u></b></i>♦️\n" + sch_data.getDataFromDB(group_id="11_1", day=DAYS[6-i]))
        await bot.send_message(callback_query.from_user.id, text="⭐️⭐️⭐️⭐️⭐️⭐️")


@dp.callback_query_handler(text="fiz-1")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.answer(text="Специальность: ФИЗ")
    await bot.send_message(callback_query.from_user.id, text=SELECTED_FIZ)
    for i in range(1, 7):
        await bot.send_message(callback_query.from_user.id, text=f"<b><i>{end_week_day}</i></b>\n \n♦️<i><b><u>{DAYS_RU[6-i]}</u></b></i>♦️\n" + sch_data.getDataFromDB(group_id="18_1", day=DAYS[6-i]))
        await bot.send_message(callback_query.from_user.id, text="⭐️⭐️⭐️⭐️⭐️⭐️")


@dp.callback_query_handler(text="mi-1")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.answer(text="Специальность: МИ")
    await bot.send_message(callback_query.from_user.id, text=SELECTED_MI)
    for i in range(1, 7):
        # 17_1
        await bot.send_message(callback_query.from_user.id, text=f"<b><i>{end_week_day}</i></b>\n \n♦️<i><b><u>{DAYS_RU[6-i]}</u></b></i>♦️\n" + sch_data.getDataFromDB(group_id="17_1", day=DAYS[6-i]))
        await bot.send_message(callback_query.from_user.id, text="⭐️⭐️⭐️⭐️⭐️⭐️")


@dp.callback_query_handler(text="web-1")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.answer(text="Специальность: ВЕБ")
    await bot.send_message(callback_query.from_user.id, text=SELECTED_WEB)
    for i in range(1, 7):
        # 12_1
        await bot.send_message(callback_query.from_user.id, text=f"<b><i>{end_week_day}</i></b>\n \n♦️<i><b><u>{DAYS_RU[6-i]}</u></b></i>♦️\n" + sch_data.getDataFromDB(group_id="12_1", day=DAYS[6-i]))
        await bot.send_message(callback_query.from_user.id, text="⭐️⭐️⭐️⭐️⭐️⭐️")


@dp.callback_query_handler(text="pm-1")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.answer(text="Специальность: ПМ")
    await bot.send_message(callback_query.from_user.id, text=SELECTED_PM)
    for i in range(1, 7):
        # 15
        await bot.send_message(callback_query.from_user.id, text=f"<b><i>{end_week_day}</i></b>\n \n♦️<i><b><u>{DAYS_RU[6-i]}</u></b></i>♦️\n" + sch_data.getDataFromDB(group_id="15_1", day=DAYS[6-i]))
        await bot.send_message(callback_query.from_user.id, text="⭐️⭐️⭐️⭐️⭐️⭐️")


@dp.callback_query_handler(text="poit-1")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.answer(text="Специальность: ПОИТ")
    await bot.send_message(callback_query.from_user.id, text=SELECTED_POIT)
    for i in range(1, 7):
        # 14
        await bot.send_message(callback_query.from_user.id, text=f"<b><i>{end_week_day}</i></b>\n \n♦️<i><b><u>{DAYS_RU[6-i]}</u></b></i>♦️\n" + sch_data.getDataFromDB(group_id="14_1", day=DAYS[6-i]))
        await bot.send_message(callback_query.from_user.id, text="⭐️⭐️⭐️⭐️⭐️⭐️")


@dp.callback_query_handler(text="isit-1")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.answer(text="Специальность: ИСИТ")
    await bot.send_message(callback_query.from_user.id, text=SELECTED_ISIT)
    for i in range(1, 7):
        # 16
        await bot.send_message(callback_query.from_user.id, text=f"<b><i>{end_week_day}</i></b>\n \n♦️<i><b><u>{DAYS_RU[6-i]}</u></b></i>♦️\n" + sch_data.getDataFromDB(group_id="16_1", day=DAYS[6-i]))
        await bot.send_message(callback_query.from_user.id, text="⭐️⭐️⭐️⭐️⭐️⭐️")


@dp.callback_query_handler(text="uir-2")  # Колбэк на УИР
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.answer(text="Специальность: УИР")
    await bot.send_message(callback_query.from_user.id, text=SELECTED_UIR)
    for i in range(1, 7):
        await bot.send_message(callback_query.from_user.id, text=f"<b><i>{end_week_day}</i></b>\n \n♦️<i><b><u>{DAYS_RU[6-i]}</u></b></i>♦️\n" + sch_data.getDataFromDB(group_id="13_2", day=DAYS[6-i]))
        await bot.send_message(callback_query.from_user.id, text="⭐️⭐️⭐️⭐️⭐️⭐️")


@dp.callback_query_handler(text="poks-2")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.answer(text="Специальность: ПОКС")
    await bot.send_message(callback_query.from_user.id, text=SELECTED_POKS)
    for i in range(1, 7):
        await bot.send_message(callback_query.from_user.id, text=f"<b><i>{end_week_day}</i></b>\n \n♦️<i><b><u>{DAYS_RU[6-i]}</u></b></i>♦️\n" + sch_data.getDataFromDB(group_id="11_2", day=DAYS[6-i]))
        await bot.send_message(callback_query.from_user.id, text="⭐️⭐️⭐️⭐️⭐️⭐️")


@dp.callback_query_handler(text="fiz-2")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.answer(text="Специальность: ФИЗ")
    await bot.send_message(callback_query.from_user.id, text=SELECTED_FIZ)
    for i in range(1, 7):
        await bot.send_message(callback_query.from_user.id, text=f"<b><i>{end_week_day}</i></b>\n \n♦️<i><b><u>{DAYS_RU[6-i]}</u></b></i>♦️\n" + sch_data.getDataFromDB(group_id="18_2", day=DAYS[6-i]))
        await bot.send_message(callback_query.from_user.id, text="⭐️⭐️⭐️⭐️⭐️⭐️")


@ dp.callback_query_handler(text="mi-2")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.answer(text="Специальность: МИ")
    await bot.send_message(callback_query.from_user.id, text=SELECTED_MI)
    for i in range(1, 7):
        await bot.send_message(callback_query.from_user.id, text=f"<b><i>{end_week_day}</i></b>\n \n♦️<i><b><u>{DAYS_RU[6-i]}</u></b></i>♦️\n" + sch_data.getDataFromDB(group_id="17_2", day=DAYS[6-i]))
        await bot.send_message(callback_query.from_user.id, text="⭐️⭐️⭐️⭐️⭐️⭐️")


@ dp.callback_query_handler(text="web-2")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.answer(text="Специальность: ВЕБ")
    await bot.send_message(callback_query.from_user.id, text=SELECTED_WEB)
    for i in range(1, 7):
        await bot.send_message(callback_query.from_user.id, text=f"<b><i>{end_week_day}</i></b>\n \n♦️<i><b><u>{DAYS_RU[6-i]}</u></b></i>♦️\n" + sch_data.getDataFromDB(group_id="12_2", day=DAYS[6-i]))
        await bot.send_message(callback_query.from_user.id, text="⭐️⭐️⭐️⭐️⭐️⭐️")


@ dp.callback_query_handler(text="pm-2")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.answer(text="Специальность: ПМ")
    await bot.send_message(callback_query.from_user.id, text=SELECTED_PM)
    for i in range(1, 7):
        await bot.send_message(callback_query.from_user.id, text=f"<b><i>{end_week_day}</i></b>\n \n♦️<i><b><u>{DAYS_RU[6-i]}</u></b></i>♦️\n" + sch_data.getDataFromDB(group_id="15_2", day=DAYS[6-i]))
        await bot.send_message(callback_query.from_user.id, text="⭐️⭐️⭐️⭐️⭐️⭐️")


@ dp.callback_query_handler(text="poit-2")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.answer(text="Специальность: ПОИТ")
    await bot.send_message(callback_query.from_user.id, text=SELECTED_POIT)
    for i in range(1, 7):
        await bot.send_message(callback_query.from_user.id, text=f"<b><i>{end_week_day}</i></b>\n \n♦️<i><b><u>{DAYS_RU[6-i]}</u></b></i>♦️\n" + sch_data.getDataFromDB(group_id="14_2", day=DAYS[6-i]))
        await bot.send_message(callback_query.from_user.id, text="⭐️⭐️⭐️⭐️⭐️⭐️")


@ dp.callback_query_handler(text="isit-2")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.answer(text="Специальность: ИСИТ")
    await bot.send_message(callback_query.from_user.id, text=SELECTED_ISIT)
    for i in range(1, 7):
        await bot.send_message(callback_query.from_user.id, text=f"<b><i>{end_week_day}</i></b>\n \n♦️<i><b><u>{DAYS_RU[6-i]}</u></b></i>♦️ \n" + sch_data.getDataFromDB(group_id="16_2", day=DAYS[6-i]))
        await bot.send_message(callback_query.from_user.id, text="⭐️⭐️⭐️⭐️⭐️⭐️")


@ dp.message_handler(commands=['start', 'get_schedule'])
async def start_message(message: types.Message):
    db.add_user(user_id=message.from_user.id)
    await bot.send_message(message.chat.id, text=START_MESSAGE.format(message.from_user.first_name), reply_markup=group_keyboard)


@ dp.message_handler(commands=["sub"])
async def subscribe(message: types.Message):
    db.subscribe(user_id=message.from_user.id)
    await bot.send_message(message.chat.id, text=SUBSCRIBED)


@ dp.message_handler(commands=["unsub"])
async def unsubscribe(message: types.Message):
    db.unsubscribe(user_id=message.from_user.id)
    await bot.send_message(message.chat.id, text=UNSUBSCRIBED)


@ dp.message_handler(commands=['status'])
async def status(message: types.Message):
    if (db.is_subscribed(user_id=message.from_user.id)):
        await bot.send_message(message.chat.id, text=STATUS_TRUE)
    else:
        await bot.send_message(message.chat.id, text=STATUS_FALSE)

@dp.message_handler(commands=['get_file_xlsx'])
async def send_xlsx_file(message: types.Message):
    with open(get_xlsx_name(), "rb") as file:
        await bot.send_document(message.chat.id, types.InputFile(file))
# async def new_schedule(wait_for: int):
#     while True:
#         await asyncio.sleep(wait_for)
#         now = datetime.utcnow()
#         await bot.send_message  (chat_id=756764405, text=str(now)[:19])
# async def get_file_name(SITE_LINK):
    
#     response = requests.get(url=SITE_LINK)
#     response.raise_for_status()
    
#     soup = BeautifulSoup(response.text, "lxml")
#     table = soup.find('table', {"class": "table table-bordered"})
#     tbody = table.find('tbody')
#     td = tbody.find("td")
#     pattern = re.compile(".*Расписание_занятий_1_курс.*")
#     link = next((link.get('href') for link in td.find_all('a')
#                    if pattern.match(link.get('href'))), None)
#     pattern = re.compile(r"\d{2}.\d{2}.\d{4}-\d{2}.\d{2}.\d{4}")
#     result = pattern.search(link)
#     # print(result.group())
#     return  result.group()


# async def check_and_download(time_to_wait: int, SITE_LINK):
#     mes = await get_file_name(SITE_LINK)
#     print(mes)
#     await asyncio.sleep(time_to_wait)

if __name__ == "__main__":
    # asyncio.get_event_loop().create_task(check_and_download(3, SITE_LINK))
    executor.start_polling(dp, skip_updates=True)
