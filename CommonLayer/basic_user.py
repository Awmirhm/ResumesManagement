from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname

    @abstractmethod
    def create_with_tuple(self, data: tuple):
        pass

    @abstractmethod
    def create_whit_list(self, data: list):
        pass
