from datetime import date
import re
from DataAccessLayer.form_data_access import FormDataAccess


class FormBusiness:
    def __init__(self):
        self.form_data_access = FormDataAccess()

    def get_form(self, firstname, lastname, birthday, gender: int, skills, email, image):
        pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if len(firstname) < 3:
            return [None, "First Name Length should be least 3"]
        if any(char.isdigit() for char in firstname):
            return [None, "The First Name does not have a number"]

        if len(lastname) < 3:
            return [None, "Last Name Length should be least 3"]
        if any(char.isdigit() for char in lastname):
            return [None, "The Last Name does not have a number"]

        try:
            date_value = date.fromisoformat(birthday)
        except ValueError:
            return [None, "Date Format is wrong, ex : 2014-01-01"]

        if gender == 0:
            return [None, "Please select your gender"]

        if len(skills) < 6:
            return [None, "Skills Length should be least 6"]

        if len(email) < 6:
            return [None, "Email Length should be least 6"]
        if not re.match(pat, email):
            return [None, "Invalid Email"]

        if not image:
            return [None, "Please Choose your photo"]

        else:
            self.form_data_access.get_form(firstname, lastname, date_value, gender, skills, email, image)
            return ["Your information has been sent successfully \n You will be notified by email", None]

    def update_status_to_accept(self, form_id):
        self.form_data_access.update_status(2, form_id)

    def update_status_to_reject(self, form_id):
        self.form_data_access.update_status(3, form_id)


class FormIterator:
    def __init__(self, index=1):
        self.form_data_access = FormDataAccess()
        self.__index = index

    def __iter__(self):
        return self

    def __next__(self):
        try:
            form = self.form_data_access.get_resumes(self.__index)
            self.__index += 1
            return form
        except TypeError:
            raise StopIteration
