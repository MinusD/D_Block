from Task1.LogModule import *


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        Log('CRE', f'создано Person - {name}')

