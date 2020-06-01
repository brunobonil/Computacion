class Person:

    def __init__(self, name=None, surname=None, age=None):
        self._name = name
        self._surname = surname
        self._age = age

    @property
    def name(self):
        return self._name.upper()

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def surname(self):
        return self._surname.upper()

    @surname.setter
    def surname(self, value):
        self._surname = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
