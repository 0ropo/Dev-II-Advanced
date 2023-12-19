import unittest
from utils.classes.table import Table 

class TestTable(unittest.TestCase):

    def setUp(self):
        # Créez une instance de la classe Table pour les tests
        self.table = Table(numTable=1, capaciteTable=4, idService="V")

    def test_initialization(self):
        self.assertEqual(self.table.numTable, 1)
        self.assertEqual(self.table.capaciteTable, 4)
        self.assertEqual(self.table.idService, "V")

    def test_numTable_getter(self):
        self.assertEqual(self.table.numTable, 1)

        # essayer d'accéder à l'attribut privé et de le modifier ce qui devrait pas fonctionner
        with self.assertRaises(AttributeError):
            self.table.numTable = 2

    def test_numTable_setter(self):
        self.table.numTable = 2
        self.assertEqual(self.table.numTable, 2)

        with self.assertRaises(ValueError):
            self.table.numTable = 0

        with self.assertRaises(TypeError):
            self.table.numTable = "invalid"

    def test_capaciteTable_setter(self):
        self.table.capaciteTable = 15
        self.assertEqual(self.table.capaciteTable, 15)

        with self.assertRaises(ValueError):
            self.table.capaciteTable = 10

        with self.assertRaises(TypeError):
            self.table.capaciteTable = "invalid"

    def test_idService_setter(self):
        self.table.idService = "B"
        self.assertEqual(self.table.idService, "B")

        with self.assertRaises(ValueError):
            self.table.idService = "invalid"

        with self.assertRaises(TypeError):
            self.table.idService = 123

    def test_to_json(self):
        expected_json = {"numTable": 1, "capaciteTable": 4, "idService": "V"}
        self.assertEqual(self.table.to_json(), expected_json)

    def test_from_json(self):
        json_data = {"numTable": 3, "capaciteTable": 2, "idService": "B"}
        new_table = Table.from_json(json_data)

        self.assertEqual(new_table.numTable, 3)
        self.assertEqual(new_table.capaciteTable, 2)
        self.assertEqual(new_table.idService, "B")

if __name__ == '__main__':
    unittest.main()
