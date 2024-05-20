from .basic_user import User


class UsersAdmin(User):
    def __init__(self, id, firstname, lastname, username, password):
        super().__init__(id, firstname, lastname)

        self.username = username
        self.password = password

    @classmethod
    def create_with_tuple(cls, data: tuple):
        return cls(data[0], data[1], data[2], data[3], data[4])

    @classmethod
    def create_whit_list(cls, data: list):
        return cls(data[0], data[1], data[2], data[3], data[4])
