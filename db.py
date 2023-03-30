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

            for i in range(11, 19):

                value = f'{i}'+'_'+'1'
                cursor.execute(
                    """INSERT OR IGNORE INTO schedule('group_id') VALUES(?)""", ((value), ))
                value = f'{i}'+'_'+'2'
                cursor.execute(
                    """INSERT OR IGNORE INTO schedule('group_id') VALUES(?)""", ((value), ))

            # for i in range(6):
            #     for j in range(1, 9):
            #             value = getDaySch(
            #                 sheet=get_ws()[0], day_start=RANGES_DAYS[i][0], day_end=RANGES_DAYS[i][1], group=RANGES_GROUPS[f"1{j}"][0])
            #             cursor.execute(
            #                 f"""UPDATE schedule SET {DAYS[i]} = ? WHERE group_id =?""", (value, f"1{j}_1"))
            #             value1 = getDaySch(
            #                 sheet=get_ws()[0], day_start=RANGES_DAYS[i][0], day_end=RANGES_DAYS[i][1], group=RANGES_GROUPS[f"1{j}"][1])
            #             cursor.execute(
            #                 f"""UPDATE schedule SET {DAYS[i]} = ? WHERE group_id =?""", (value1, f"1{j}_2"))
            #             connection.commit()
        except Exception as ex:
            print(ex)
        finally:
            cursor.close()
            connection.close()


def update_schedule():
        connection = sqlite3.connect(
            "schedule_db.db", check_same_thread=False)
        cursor = connection.cursor()
        try:
            for i in range(6):
                for j in range(1, 9):
                        value = getDaySch(
                            sheet=get_ws()[0], day_start=RANGES_DAYS[i][0], day_end=RANGES_DAYS[i][1], group=RANGES_GROUPS[f"1{j}"][0])
                        cursor.execute(
                            f"""UPDATE schedule SET {DAYS[i]} = ? WHERE group_id =?""", (value, f"1{j}_1"))
                        value1 = getDaySch(
                            sheet=get_ws()[0], day_start=RANGES_DAYS[i][0], day_end=RANGES_DAYS[i][1], group=RANGES_GROUPS[f"1{j}"][1])
                        cursor.execute(
                            f"""UPDATE schedule SET {DAYS[i]} = ? WHERE group_id =?""", (value1, f"1{j}_2"))
                        connection.commit()
        except Exception as ex:
            print("Ошибка в db.py update_schedule: " + str(ex))
        finally:
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
