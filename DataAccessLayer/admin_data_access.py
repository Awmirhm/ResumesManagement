import sqlite3
from CommonLayer.users_admin import UsersAdmin


class AdminDataAccess:
    def __init__(self):
        self.data_base_name = "ResumesManagement.db"

    def get_user(self, username, password):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                    SELECT id,
                           first_name,
                           last_name,
                           username,
                           password
                    FROM Users_Admin
                    WHERE  username = ?
                    AND   password = ?""", [username, password]).fetchone()

            if data:
                user = UsersAdmin.create_with_tuple(data)
                return user
            else:
                return None
