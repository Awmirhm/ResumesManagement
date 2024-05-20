import sqlite3
from CommonLayer.users_form import UsersForm


class FormDataAccess:
    def __init__(self):
        self.data_base_name = "ResumesManagement.db"

    def get_form(self, firstname, lastname, birthday, gender, skills, email, image):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                    INSERT INTO Users_Form (
                                   first_name,
                                   last_name,
                                   birthday,
                                   gener_id,
                                   skills,
                                   email,
                                   image
                               )
                               VALUES (
                                   ?,
                                   ?,
                                   ?,
                                   ?,
                                   ?,
                                   ?,
                                   ?
                               )""", [firstname, lastname, birthday, gender, skills, email, image])
            connection.commit()
