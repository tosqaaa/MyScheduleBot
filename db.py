import sqlite3
from Exceler import getDaySch, ws
from keys import RANGES_DAYS, RANGES_GROUPS, DAYS, exec_time


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


class ScheduleData:
    @exec_time
    def __init__(self, to_update: bool):
        self.connection = sqlite3.connect(
            "schedule_db.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS schedule(
                    group_id TEXT,
                    Monday TEXT,
                    Tuesday TEXT,
                    Wednesday TEXT,
                    Thursday TEXT,
                    Friday TEXT,
                    Sunday TEXT)""")
            self.connection.commit()

            for i in range(11, 20):

                value = f'{i}'+'_'+'1'
                self.cursor.execute(
                    """INSERT OR IGNORE INTO schedule('group_id') VALUES(?)""", ((value), ))
                value = f'{i}'+'_'+'2'
                self.cursor.execute(
                    """INSERT OR IGNORE INTO schedule('group_id') VALUES(?)""", ((value), ))
            if to_update is True:
                for i in range(6):
                    for j in range(1, 9):
                        value = getDaySch(
                            sheet=ws, day_start=RANGES_DAYS[i][0], day_end=RANGES_DAYS[i][1], group=RANGES_GROUPS[f"1{j}"][0])
                        self.cursor.execute(
                            f"""UPDATE schedule SET {DAYS[i]} = ? WHERE group_id =?""", (value, f"1{j}_1"))
                        value1 = getDaySch(
                            sheet=ws, day_start=RANGES_DAYS[i][0], day_end=RANGES_DAYS[i][1], group=RANGES_GROUPS[f"1{j}"][1])
                        self.cursor.execute(
                            f"""UPDATE schedule SET {DAYS[i]} = ? WHERE group_id =?""", (value1, f"1{j}_2"))
                        self.connection.commit()
        except Exception as ex:
            print(ex)
        finally:
            self.cursor.close()
            self.connection.close()

    def getDataFromDB(self, group_id, day):
        self.connection = sqlite3.connect(
            "schedule_db.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        try:
            result = self.cursor.execute(
                f"""SELECT {day} FROM schedule WHERE group_id = ? """, (group_id,)).fetchone()
            return result[0]

        except Exception as ex:
            print(ex)
        finally:
            self.cursor.close
            self.connection.close



