import sqlite3
from CommonLayer.users_form import UsersForm
from io import BytesIO


class FormDataAccess:
    def __init__(self):
        self.data_base_name = "ResumesManagement.db"

    def get_form(self, firstname, lastname, birthday, gender, skills, email, image):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
        INSERT INTO Users_Form (
                                   first_name,
                                   last_name,
                                   birthday,
                                   gener_id,
                                   skills,
                                   email,
                                   image,
                                   status
                               )
                               VALUES (
                                   ?,
                                   ?,
                                   ?,
                                   ?,
                                   ?,
                                   ?,
                                   ?,
                                   "{0}")""", [firstname, lastname, birthday, gender, skills, email, image])
            connection.commit()

    def get_resumes(self, form_id):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                SELECT id,
                       first_name,
                       last_name,
                       birthday,
                       gener_id,
                       skills,
                       email,
                       image,
                       status
                FROM Users_Form
                WHERE  id = ?""", [form_id]).fetchone()
            form = UsersForm.create_with_tuple(data)
            return form

    def update_status(self, status, form_id):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                    UPDATE Users_Form
                    SET status = ?
                    WHERE id = ?
                    """, [status, form_id])

            connection.commit()
