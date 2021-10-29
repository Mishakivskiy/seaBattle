import sqlite3
import BotLogic

class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def addroom(self, id, first_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `rooms` (`id`, `user1_id`,`user2_id`) VALUES(?,?,?)",(id, first_id, 0))

    def check_id(self, RoomID):
        with self.connection:
            self.cursor.execute(f"SELECT `id` FROM `rooms` WHERE `id` = {RoomID}")
            return self.cursor.fetchone()

    def check2nd(self, RoomID):
        with self.connection:
            self.cursor.execute(f"SELECT `user2_id` FROM `rooms` WHERE `id` = {RoomID}")
            id = BotLogic.clean_userID(str(self.cursor.fetchone()))
            if id == 0: return False
            else: return True

    def second_connect(self, user_id, RoomID):
        with self.connection:
            return self.cursor.execute("UPDATE `rooms` SET `user2_id` = ? WHERE `id` = ?", (user_id, RoomID))

    def try_start(self, roomID):
        with self.connection:
            self.cursor.execute(f"SELECT `user2_id` FROM `rooms` WHERE `id` = {roomID}")
            el = str(self.cursor.fetchone())

            ID2 = BotLogic.clean_userID(el)

            self.cursor.execute(f"SELECT `user1_id` FROM `rooms` WHERE `id` = {roomID}")
            el = str(self.cursor.fetchone())

            ID1 = BotLogic.clean_userID(el)

            IDs = [ID1, ID2]

            return IDs

    def close(self):
        self.connection.close()