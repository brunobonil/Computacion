from repository import Repository
from person import Person


class PersonService:

    def get_personList(self):
        for i in Repository.person:
            print("ID ->", i, Repository.person[i])

    def add_person(self, person=None):
        if person is None:
            p1 = Person()
            p1.name = input("Nombre: ")
            p1.surname = input("Apellido: ")
            p1.age = (input("Edad: "))
            person = p1
        lastKey = -1
        for key in Repository.person:
            lastKey = key
        lastKey = lastKey + 1
        Repository.person[lastKey] = {'_name': person.name,
                                      '_surname': person.surname,
                                      '_age': person.age}

    def update_person(self, key=None, person=None):
        if key is None and person is None:
            key = int(input("Ingrese la key de la persona: "))
            p1 = Person()
            p1.name = input("Nombre: ")
            p1.surname = input("Apellido: ")
            p1.age = (input("Edad: "))
            person = p1
        dicc = Repository.person
        dicc[key] = {'_name': person.name,
                     '_surname': person.surname,
                     '_age': person.age}

    def delete_person(self, key=None):
        if key is None:
            key = int(input("Ingrese la key de la persona a eliminar: "))
        dicc = Repository.person
        del dicc[key]
