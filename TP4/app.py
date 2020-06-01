from person import Person
from personService import PersonService


class App():
    def __init__(self):
        self.person = Person()

    def menu(self):
        print("Administrar Personas")
        print("1. Agregar persona")
        print("2. Modificar persona")
        print("3. Eliminar persona")
        print("4. Listar personas")
        return int(input("Elija una opción:"))


if __name__ == "__main__":
    app = App()
    while True:
        op = app.menu()
        personService = PersonService()
        if op == 1:
            personService.add_person()
        if op == 2:
            personService.update_person()
        if op == 3:
            personService.delete_person()
        if op == 4:
            personService.get_personList()
