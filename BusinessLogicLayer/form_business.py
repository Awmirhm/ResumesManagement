from datetime import date


class FormBusiness:
    def __init__(self):
        pass

    def get_form(self, firstname, lastname, birthday, gender: int, skills, email, image):

        email_requirements_at_the_rate = ["@"]
        email_requirements = ["email", "gmail", "yahoo"]

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