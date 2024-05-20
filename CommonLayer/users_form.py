from .basic_user import User
from .descriptor import LengthDescriptor
from .descriptor import DateDescriptor


class UsersForm(User):
    birthday = DateDescriptor()
    skills = LengthDescriptor(6)
    email = LengthDescriptor(6)

    def __init__(self, id, firstname, lastname, birthday, gender, skills, email, image):
        super().__init__(id, firstname, lastname)

        self.birthday = birthday
        self.gender = gender
        self.skills = skills
        self.email = email
        self.image = image

    @classmethod
    def create_with_tuple(cls, data: tuple):
        return cls(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])

    @classmethod
    def create_whit_list(cls, data: list):
        return cls(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
