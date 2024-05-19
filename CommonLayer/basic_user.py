from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname

    @abstractmethod
    def create_with_tuple(self, data: tuple):
        pass


class UsersForm(User):
    def __init__(self, id, firstname, lastname, birthday, gender, skills, email):
        super().__init__(id, firstname, lastname)

        self.birthday = birthday
        self.gender = gender
        self.skills = skills
        self.email = email

    @classmethod
    def create_with_tuple(cls, data: tuple):
        return cls(data[0], data[1], data[2], data[3], data[4], data[5], data[6])

