from abc import ABC, abstractmethod
from .descriptor import LengthDescriptor


class User(ABC):
    firstname = LengthDescriptor(3)
    lastname = LengthDescriptor(3)

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
