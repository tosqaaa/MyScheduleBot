import sqlite3
from Exceler import getDaySch, get_ws
from keys import RANGES_DAYS, RANGES_GROUPS, DAYS, exec_time
import os


class Subscriber:
    def __init__(self):
        self.connection = sqlite3.connect("users.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
               user_id INT PRIMARY KEY,
                status INT)""")

    def add_user(self, user_id, status=True):
        self.connection = sqlite3.connect("users.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(
                """INSERT OR IGNORE INTO users ('user_id', 'status') VALUES(?, ?)""", (user_id, status))
            self.connection.commit()
        except Exception as ex:
            return ex
        finally:
            self.cursor.close
            self.connection.close

    def unsubscribe(self, user_id, status=False):
        self.connection = sqlite3.connect("users.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(
                """UPDATE users SET status = ? WHERE user_id =?""", (status, user_id))
            self.connection.commit()
        except Exception as ex:
            return ex
        finally:
            self.cursor.close()
            self.connection.close()

    def subscribe(self, user_id, status=True):
        self.connection = sqlite3.connect("users.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(
                """UPDATE users SET status = ? WHERE user_id =?""", (status, user_id))
            self.connection.commit()
        except Exception as ex:
            return ex

        finally:
            self.cursor.close()
            self.connection.close()

    def is_subscribed(self, user_id):
        self.connection = sqlite3.connect("users.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        try:
            status = self.cursor.execute(
                f"""SELECT status FROM users WHERE user_id = '{user_id}'""").fetchall()
            return bool(status[0][0])
        except Exception as ex:
            return ex
        finally:
            self.cursor.close()
            self.connection.close()


@exec_time
def create_schedule_db():
        connection = sqlite3.connect(
            "schedule_db.db", check_same_thread=False)
        cursor = connection.cursor()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS schedule(
                    group_id TEXT,
                    Monday TEXT,
                    Tuesday TEXT,
                    Wednesday TEXT,
                    Thursday TEXT,
                    Friday TEXT,
                    Sunday TEXT)""")
            connection.commit()
            sheet, _ = get_ws()
            for i in range(11, 19):
                value = f'{i}'+'_'+'1'
                cursor.execute(
                    """INSERT OR IGNORE INTO schedule('group_id') VALUES(?)""", ((value), ))
                value = f'{i}'+'_'+'2'
                cursor.execute(
                    """INSERT OR IGNORE INTO schedule('group_id') VALUES(?)""", ((value), ))
            for group_num in range(11, 19):
                group_id = f"1{group_num}_"
                for day_idx, day_name in enumerate(DAYS):
                # получаем значение расписания для первой и второй подгруппы
                        value = getDaySch(
                        sheet=sheet,
                        day_start=RANGES_DAYS[day_idx][0],
                        day_end=RANGES_DAYS[day_idx][1],
                        group=RANGES_GROUPS[f"{group_num}"][0]
                        )
                        value1 = getDaySch(
                            sheet=sheet,
                            day_start=RANGES_DAYS[day_idx][0],
                            day_end=RANGES_DAYS[day_idx][1],
                            group=RANGES_GROUPS[f"{group_num}"][1]
                        )

                # обновляем значения в базе данных
                cursor.execute(
                    f"UPDATE schedule SET {day_name} = ? WHERE group_id = ?", (value, f"{group_id}1")
                )
                cursor.execute(
                    f"UPDATE schedule SET {day_name} = ? WHERE group_id = ?", (value1, f"{group_id}2")
                )

        # сохраняем изменения в базе данных
            connection.commit()
        except Exception as ex:
            print(ex)
        finally:
            cursor.close()
            connection.close()
@exec_time
def update_schedule():
    try:
        # открываем соединение с базой данных
        connection = sqlite3.connect("schedule_db.db", check_same_thread=False)
        cursor = connection.cursor()

        # получаем лист с расписанием и группы
        sheet, _ = get_ws()

        # для каждой группы и дня недели
        for group_num in range(11, 19):
            group_id = f"1{group_num}_"
            for day_idx, day_name in enumerate(DAYS):
                # получаем значение расписания для первой и второй подгруппы
                value = getDaySch(
                    sheet=sheet,
                    day_start=RANGES_DAYS[day_idx][0],
                    day_end=RANGES_DAYS[day_idx][1],
                    group=RANGES_GROUPS[f"{group_num}"][0]
                )
                value1 = getDaySch(
                    sheet=sheet,
                    day_start=RANGES_DAYS[day_idx][0],
                    day_end=RANGES_DAYS[day_idx][1],
                    group=RANGES_GROUPS[f"{group_num}"][1]
                )

                # обновляем значения в базе данных
                cursor.execute(
                    f"UPDATE schedule SET {day_name} = ? WHERE group_id = ?", (value, f"{group_id}1")
                )
                cursor.execute(
                    f"UPDATE schedule SET {day_name} = ? WHERE group_id = ?", (value1, f"{group_id}2")
                )

        # сохраняем изменения в базе данных
        connection.commit()
    except Exception as ex:
        print("Ошибка в db.py update_schedule: " + str(ex))
    finally:
        # закрываем соединение с базой данных
        cursor.close()
        connection.close()

def getDataFromDB (group_id, day):
        connection = sqlite3.connect(
            "schedule_db.db", check_same_thread=False)
        cursor = connection.cursor()
        try:
            result = cursor.execute(
                f"""SELECT {day} FROM schedule WHERE group_id = ? """, (group_id,)).fetchone()
            return result[0]

        except Exception as ex:
            print(ex)
        finally:
            cursor.close
            connection.close
            
create_schedule_db()

