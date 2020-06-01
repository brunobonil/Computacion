import unittest
from repository import Repository
from person import Person
from personService import PersonService
from parameterized import parameterized


class TestPerson(unittest.TestCase):

    @parameterized.expand([
        ("Bruno", "Bonil", 19, 0, {'_name': "BRUNO", '_surname': "BONIL",
                                   '_age': 19}),
        ("Juan", "Perez", 24, 1, {'_name': "JUAN", '_surname': "PEREZ",
                                  '_age': 24}),
        ("Miguel", "Sanchez", 54, 2, {'_name': "MIGUEL", '_surname': "SANCHEZ",
                                      '_age': 54})
    ])
    def test_agregar(self, name, surname, age, key, dic):
        p1 = Person(name, surname, age)
        add = PersonService()
        add.add_person(p1)
        self.assertEqual(Repository.person[key], dic)

    @parameterized.expand([
        ("Bruno", "Bonil", 19, 0, {'_name': "BRUNO", '_surname': "BONIL",
                                   '_age': 19}),
        ("Juan", "Garcia", 24, 1, {'_name': "JUAN", '_surname': "GARCIA",
                                   '_age': 24}),
        ("Martin", "Sanchez", 54, 2, {'_name': "MARTIN", '_surname': "SANCHEZ",
                                      '_age': 54})
    ])
    def test_modificar(self, name, surname, age, key, dic):
        p1 = Person(name, surname, age)
        update = PersonService()
        update.update_person(key, p1)
        self.assertEqual(Repository.person[key], dic)

    @parameterized.expand([
        (0, ),
        (1, ),
        (2, )
    ])
    def test_delete(self, key):
        delete = PersonService()
        delete.delete_person(key)
        lista = Repository.person
        self.assertNotIn(key, lista.keys())


if __name__ == "__main__":
    unittest.main()
