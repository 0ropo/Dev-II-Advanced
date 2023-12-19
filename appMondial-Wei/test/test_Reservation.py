import unittest
from utils.classes.reservation import Reservation  


class TestReservation(unittest.TestCase):

    def setUp(self):
        """ Initialisation commune pour tous les tests """
        self.valid_reservation = Reservation("Nom", "0123456789", 1, "2023-12-12 18:00", "eu", 0, 0, 1, 1)

    def test_initialisation_valide(self):
        """ Test de l'initialisation avec des valeurs valides """
        self.assertEqual(self.valid_reservation.nom, "Nom")
        self.assertEqual(self.valid_reservation.telNum, "0123456789")
        self.assertEqual(self.valid_reservation.numTable, 1)
        self.assertEqual(self.valid_reservation.dateHeure, "2023-12-12 18:00")
        self.assertEqual(self.valid_reservation.idCuisine, "eu")
        self.assertEqual(self.valid_reservation.pmr, 0)
        self.assertEqual(self.valid_reservation.bb, 0)
        self.assertEqual(self.valid_reservation.nbrClient, 1)
        self.assertEqual(self.valid_reservation.idRes, 1)

    def test_setters_valides(self):
        """ Test des setters avec des valeurs valides """
        self.valid_reservation.nom = "Autre Nom"
        self.valid_reservation.telNum = "9876543210"
        self.valid_reservation.numTable = 2
        self.valid_reservation.idCuisine = "af"
        self.valid_reservation.pmr = 1
        self.valid_reservation.bb = 1
        self.valid_reservation.nbrClient = 2
        self.valid_reservation.idRes = 2

        self.assertEqual(self.valid_reservation.nom, "Autre Nom")
        self.assertEqual(self.valid_reservation.telNum, "9876543210")
        self.assertEqual(self.valid_reservation.numTable, 2)
        self.assertEqual(self.valid_reservation.idCuisine, "af")
        self.assertEqual(self.valid_reservation.pmr, 1)
        self.assertEqual(self.valid_reservation.bb, 1)
        self.assertEqual(self.valid_reservation.nbrClient, 2)
        self.assertEqual(self.valid_reservation.idRes, 2)

    def test_setters_invalides(self):
        """ Test des setters avec des valeurs invalides """
        with self.assertRaises(TypeError):
            self.valid_reservation.nom = 123

        with self.assertRaises(TypeError):
            self.valid_reservation.telNum = 12345

        with self.assertRaises(ValueError):
            self.valid_reservation.numTable = -1

        with self.assertRaises(ValueError):
            self.valid_reservation.idCuisine = "incorrect"

        with self.assertRaises(TypeError):
            self.valid_reservation.pmr = "invalid"

        with self.assertRaises(TypeError):
            self.valid_reservation.bb = "invalid"

        with self.assertRaises(ValueError):
            self.valid_reservation.nbrClient = 0

        with self.assertRaises(ValueError):
            self.valid_reservation.idRes = 0

    def test_to_json(self):
        """ Test de la méthode to_json """
        expected_json = {
            "nom": "Nom",
            "telNum": "0123456789",
            "numTable": 1,
            "dateHeure": "2023-12-12 18:00",
            "idCuisine": "eu",
            "pmr": 0,
            "bb": 0,
            "nbrClient": 1,
            "idRes": 1
        }
        self.assertEqual(self.valid_reservation.to_json(), expected_json)

    def test_from_json(self):
        """ Test de la méthode from_json """
        json_data = {
            "nom": "Nom",
            "telNum": "0123456789",
            "numTable": 1,
            "dateHeure": "2023-12-12 18:00",
            "idCuisine": "eu",
            "pmr": 0,
            "bb": 0,
            "nbrClient": 1,
            "idRes": 1
        }
        reservation_from_json = Reservation.from_json(json_data)
        self.assertEqual(reservation_from_json.to_json(), json_data)


if __name__ == '__main__':
    unittest.main()
