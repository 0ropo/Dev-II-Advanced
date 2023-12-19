from utils.classes.reservation import Reservation


class ReservationManager:
    def __init__(self):
        """
        Pre: --
        Post: Initialisation de l'instance avec une liste vide de réservations.
        """
        self.reservations = []

    def addReservation(self, new_reservation):
        """
        Ajoute une nouvelle réservation à la liste.

        Pre: new_reservation a ajouter.
        Post: new_reservation est ajoutée à la liste des réservations.

        raise : new_reservation doit être une instance de Reservation.
                on vérifie si l'id de la réservation n'existe pas déjà dans la liste des réservations. 
        """
        if any(res.idRes == new_reservation.idRes for res in self.reservations):
            raise ValueError("Une réservation avec le même ID existe déjà.")
        assert isinstance(new_reservation, Reservation), "Ce n'est pas une instance de Reservation"
        self.reservations.append(new_reservation)

    def findReservationById(self, reservation_id):
        for reservation in self.reservations:
            if reservation.idRes == reservation_id:
                return reservation
        return None
    
    def removeReservation(self, reservation_to_remove):
        """
        Supprime une réservation de la liste.

        Pre: reservation_to_remove a supprimer
        Post: reservation_to_remove est retirée de la liste des réservations.

        Raise : reservation_to_remove doit être une instance de Reservation 
                et faire partie de self.reservations.

        """
        
        if not isinstance(reservation_to_remove, Reservation):
            raise TypeError("L'élément à supprimer doit être une instance de Reservation.")
        if not reservation_to_remove in self.reservations: 
            raise TypeError("L'élément à supprimer doit être présente dans la liste.")
        self.reservations.remove(reservation_to_remove)
        

    def findReservationByName(self, name):
        """
        Trouve une réservation par son nom.

        Pre: name de la réservation
        Post: Retourne l'objet Reservation correspondant si trouvé, sinon renvoie None.

        Raise : name doit être une chaîne de caractères.
        """
        if not isinstance(name, str):
            raise TypeError("La valeur donnée n'est pas une chaîne de caractères.")

        for reservation in self.reservations:
            if reservation.nom == name:
                return reservation
        return None  


    def findReservationByTable(self, table):
        """
        Trouve les réservations pour une table spécifique.

        Pre: Numéro de table
        Post: Retourne une liste des réservations pour cette table. Si aucune ne correspond une liste vide sera renvoyée.

        
        Raise : table doit être un entier.
        """
        if not isinstance(table, int):
            raise TypeError("La valeur donnée n'est pas un entier.")
        reservations_for_table = []
        for reservation in self.reservations:
            if reservation.numTable == table:
                reservations_for_table.append(reservation)

        return reservations_for_table

    def affichage(self):
        """
        Affiche toutes les réservations.

        Pre: --
        Post: Affiche chaque réservation de la liste.
        """
        for reservation in self.reservations:
            print(reservation)

    
    def to_json(self):
        reservations_json = [reservations.to_json() for reservations in self.reservations]
        return {
            "reservations": reservations_json
        }

    @classmethod
    def from_json(cls, data):
        manager = cls()
        reservations_data = data.get("reservations", [])
        for reservations_data in reservations_data:
            reservations = Reservation.from_json(reservations_data)
            manager.addReservation(reservations)
        return manager
