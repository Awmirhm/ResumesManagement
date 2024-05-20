from datetime import date


class LengthDescriptor:
    def __init__(self, max_char):
        self.__max_char = max_char

    def __set_name__(self, owner, name):
        self.__attribute_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__attribute_name]

    def __set__(self, instance, value):
        if len(value) < self.__max_char:
            raise ValueError(f"Invalid Value {self.__attribute_name}")
        else:
            instance.__dict__[self.__attribute_name] = value


class DateDescriptor:
    def __set_name__(self, owner, name):
        self.__attribute_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__attribute_name]

    def __set__(self, instance, value):
        try:
            date_value = date.fromisoformat(value)
        except:
            raise ValueError(f"Invalid Value {self.__attribute_name}")
        else:
            instance.__dict__[self.__attribute_name] = date_value
