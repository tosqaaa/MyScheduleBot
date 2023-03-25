from datetime import datetime
import openpyxl
import re



SITE_LINK = "https://vsu.by/universitet/fakultety/matematiki-i-it/raspisanie.html"

BOT_TOKEN = "6290378309:AAGDGsHTCgk3BDk5abB0xZekpauu_i7Zxk0"

# RANGES_DAYS = {"Monday": [16, 40],
#                "Tuesday": [43, 66],
#                "Wendsday": [70, 94],
#                "Thursday": [97, 120],
#                "Friday": [124, 148],
#                "Sunday": [151, 175]}
RANGES_DAYS = [[16, 40], [43, 66], [70, 94], [97, 120], [124, 148], [151, 175]]
RANGES_GROUPS = {"16": ['d', 'e'],
                 "17": ['f', 'g'],
                 "12": ['h', 'i'],
                 "11": ['j', 'k'],
                 "15": ['l', 'm'],
                 "14": ['n', 'o'],
                 "13": ['p', 'q'],
                 "18": ['r', 's']}
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Sunday"]
DAYS_RU = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]


def exec_time(func):
    def timer(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        print("Время работы", f"{func}", str(end - start))
    return timer

