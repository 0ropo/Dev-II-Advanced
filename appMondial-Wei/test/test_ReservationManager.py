import unittest
from utils.classes.reservationManager import Reservation, ReservationManager
from unittest.mock import patch
from io import StringIO


class TestReservationManager(unittest.TestCase):

    def setUp(self):
        self.manager = ReservationManager()
        self.res1 = Reservation("Nom1", "0123456789", 1, "2023-12-10 18:00", "eu", 0, 0, 1, 1)
        self.res2 = Reservation("Nom2", "9876543210", 2, "2023-12-11 19:00", "af", 0, 0, 2, 2)

    def test_addReservation(self):

        #test Normal
        self.manager.addReservation(self.res1)
        self.assertIn(self.res1, self.manager.reservations)

        #test Non-Res
        self.manager.reservations = []
        non_reservation = "not a reservation object"
        with self.assertRaises(AssertionError):
            self.manager.addReservation(non_reservation)

        #test none
        self.manager.reservations = []
        with self.assertRaises(AssertionError):
            self.manager.addReservation(None)

        # multiple reservation
        self.manager.reservations = []
        self.manager.addReservation(self.res1)
        self.manager.addReservation(self.res2)
        self.assertEqual(len(self.manager.reservations), 2)
        self.assertIn(self.res1, self.manager.reservations)
        self.assertIn(self.res2, self.manager.reservations)
        
        #test duplicate id reservation
        self.manager.reservations = []
        self.manager.addReservation(self.res1)
        duplicate_res = Reservation("Nom3", "0234567891", 3, "2023-12-13 20:00", "as", 0, 0, 3, 1)  # Même ID que res1
        with self.assertRaises(ValueError):
            self.manager.addReservation(duplicate_res)

        #Ajouter un très grand nombre de réservations
        self.manager.reservations = []
        for i in range(1, 1001):
            self.manager.addReservation(Reservation(f"Nom{i}", f"{i}", i, "2023-12-12 18:00", "eu", 0, 0, i, i))
        self.assertEqual(len(self.manager.reservations), 1000)


    def test_findReservationById(self):
        self.manager.addReservation(self.res1)
        self.manager.addReservation(self.res2)

        #valid id
        found = self.manager.findReservationById(1)
        self.assertEqual(found, self.res1)

        #nonexistent_id
        found = self.manager.findReservationById(999)
        self.assertIsNone(found)

        #invalid id type
        found = self.manager.findReservationById("invalid_id")
        self.assertIsNone(found)

        #find res with empty list
        self.manager.reservations = []
        found = self.manager.findReservationById(1)
        self.assertIsNone(found)


    def test_removeReservation(self):
        self.manager.addReservation(self.res1)
        self.manager.addReservation(self.res2)

        # remove valid reservation
        self.manager.removeReservation(self.res1)
        self.assertNotIn(self.res1, self.manager.reservations)

        #remove_nonexistent_reservation
        non_existent_res = Reservation("Nom3", "0234567891", 3, "2023-12-13 20:00", "as", 0, 0, 3, 3)
        with self.assertRaises(TypeError):
            self.manager.removeReservation(non_existent_res)

        #remove not res object
        with self.assertRaises(TypeError):
            self.manager.removeReservation("not a reservation object")

        # remove in a empty list
        with self.assertRaises(TypeError):
            self.manager.removeReservation(self.res1)



    def test_findReservationByName(self):
        self.manager.addReservation(self.res1)
        self.manager.addReservation(self.res2)

        #find by valid Name
        found = self.manager.findReservationByName("Nom1")
        self.assertEqual(found, self.res1)

        #no existant name
        found = self.manager.findReservationByName("NonExistent")
        self.assertIsNone(found)

        #invalid name type
        with self.assertRaises(TypeError):
            self.manager.findReservationByName(123)
        
        #empty list
        self.manager.reservations = []
        found = self.manager.findReservationByName("Nom1")
        self.assertIsNone(found)


    def test_findReservationByTable(self):
        self.manager.addReservation(self.res1)
        self.manager.addReservation(self.res2)

        reservations = self.manager.findReservationByTable(1)
        self.assertEqual(reservations, [self.res1])

        reservations = self.manager.findReservationByTable(999)
        self.assertEqual(reservations, [])

        with self.assertRaises(TypeError):
            self.manager.findReservationByTable("invalid_table")
        
        self.manager.reservations = []
        reservations = self.manager.findReservationByTable(1)
        self.assertEqual(reservations, [])

    def test_to_json(self):
        self.manager.addReservation(self.res1)
        self.manager.addReservation(self.res2)

        # test normal
        json_data = self.manager.to_json()
        expected_json = {
            "reservations": [self.res1.to_json(), self.res2.to_json()]
        }
        self.assertEqual(json_data, expected_json)

        self.manager.reservations = []
        json_data = self.manager.to_json()
        self.assertEqual(json_data, {"reservations": []})

        


    def test_from_json(self):
        self.manager.reservations = []

        # empty data
        manager_from_json = ReservationManager.from_json({})
        self.assertEqual(len(manager_from_json.reservations), 0)

        #test normal
        json_data = {
            "reservations": [self.res1.to_json(), self.res2.to_json()]
        }
        manager_from_json = ReservationManager.from_json(json_data)
        self.assertEqual(len(manager_from_json.reservations), 2)


    @patch('sys.stdout', new_callable=StringIO)
    def test_affichage(self, mock_stdout):
        self.manager.addReservation(self.res1)
        self.manager.affichage()
        expected_output = ("ID: 1 nom :Nom1, telNum :0123456789, numTable :1, "
                           "dateHeure :2023-12-10 18:00, idCuisine :eu, pmr :0, bb :0, "
                           "nombre de personne :1\n")
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
