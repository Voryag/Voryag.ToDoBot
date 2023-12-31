import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user_to_users(self, chat_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users' (chat_id) VALUES (?) ", (chat_id,))

    def add_time_to_users(self, chat_id, time_for_attention):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET time_for_attention = ? WHERE chat_id = ?", (time_for_attention, chat_id))

    def add_day_to_notifications(self, chat_id, day):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'notifications' (chat_id, day) VALUES (?, ?)", (chat_id, day))

    def add_text_to_notifications(self, chat_id, text):
        with self.connection:
            return self.cursor.execute("UPDATE 'notifications' SET text = ? WHERE chat_id = ?", (chat_id, text))

    def add_notification_to_notification(self, chat_id, text, day):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'notifications' (chat_id, text, day) VALUES (?, ?, ?)", (chat_id, text, day))

    def set_new_quantity(self, chat_id, quantity_of_notification):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET quantity_of_notification = ? WHERE chat_id = ?", (quantity_of_notification, chat_id))

    def user_exists(self, chat_id):
        with self.connection:
            res = self.cursor.execute("SELECT COUNT(*) FROM 'users' WHERE chat_id = ?", (chat_id,)).fetchall()
            return (res)

    def get_quantity_of_notifications(self, chat_id):
        with self.connection:
            return self.cursor.execute("SELECT quantity_of_notification FROM 'users' WHERE chat_id = ?", (chat_id,)).fetchone()[0]

    def get_time(self, chat_id):
        with self.connection:
            return self.cursor.execute("SELECT time_for_attention FROM 'users' WHERE chat_id = ?", (chat_id,)).fetchone()[0]

    def get_quantity_notifiactions(self, chat_id):
        with self.connection:
            return self.cursor.execute("SELECT quantity_of_notification FROM 'users' WHERE chat_id = ?", (chat_id,)).fetchone()[0]

    def get_all_notifications(self, chat_id):
        with self.connection:
            return self.cursor.execute("SELECT id, text, day FROM 'notifications' WHERE chat_id = ?", (chat_id,)).fetchall()

    def get_id_of_all_notifications(self, chat_id):
        with self.connection:
            return self.cursor.execute("SELECT id FROM 'notifications' WHERE chat_id = ?", (chat_id,)).fetchall()

    def del_notification(self, id):
        with self.connection:
            return self.cursor.execute("DELETE FROM 'notifications' WHERE id = ?", (id,))