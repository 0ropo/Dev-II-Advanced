import cmd
import json

from utils.fonctions.attrib import attribution
from utils.fonctions.initial import initial
from utils.fonctions.argParse import argParse
from utils.fonctions.ajoutRes import ajouterReservation


class ShellView(cmd.Cmd):
    intro = 'Bienvenue dans le shell de réservation. Tapez help ou ? pour la liste des commandes.\n'
    prompt = '(Reservation) --> '
    init = initial()
    file = init.fichier_sauvegarde
    data = None
    managerRes = init.reservation_manager
    managerTable = init.table_manager
    managerService = init.typeServManager
    managerCuisine = init.typeCuisineManager

    def do_afficher(self, arg):
        """Affiche les réservations"""
        self.get_data()
        for res in self.data["reservation_manager"]["reservations"]:
            print(f'ID: {res["idRes"]}, Nom: {res["nom"]}, Téléphone: {res["telNum"]}, '
                  f'Nombre de personnes: {res["nbrClient"]}, Nombre de personnes à mobilité réduite: {res["pmr"]}, '
                  f'Nombre de bébés: {res["bb"]}, Date et heure: {res["dateHeure"]}, '
                  f'Type de cuisine: {res["idCuisine"]}')


    def do_ajouter_reservation(self, arg):
        """Ajoute une réservation
        pre:
            - nom: Le nom du client
            - tel: Le numéro de téléphone du client
            - nbPers: Le nombre de personnes
            - nbPmr: Le nombre de personnes à mobilité réduite
            - nbBb: Le nombre de bébés
            - dateHeure: La date et l'heure de la réservation
            - typeCuisine: Le type de cuisine
        Exemple : ajouter_reservation John Doe,123456789,15,1,2,2023-10-10 19:00,eu
                post: Ajoute une réservation
        """
        nom, tel, nbPers, nbPmr, nbBb, dateHeure, typeCuisine = arg.split(',')
        reservation = {"nom": nom, "tel": tel, "nbPers": nbPers, "nbPmr": nbPmr, "nbBb": nbBb, "dateHeure": dateHeure, "typeCuisine": typeCuisine}
        liste = argParse(self.managerRes, reservation)

        if liste == False:
            self.managerRes.affichage()
            return 0
        else:
            if liste[0] is False:
                self.managerRes.affichage()
                self.managerRes = liste[1]
                self.init.sauvegarder_managers()
                return 0
        if None in liste:
            print('python main.py -h')
            return 0

        liste = attribution(liste, self.managerRes, self.managerTable, self.managerCuisine)
        if liste is False:
            print("Désolé, il n'y a plus de place !")
            return 1
        ajouterReservation(liste, self.managerRes)

        self.init.sauvegarder_managers()

    def do_supprimer_reservation(self, arg):
        """Supprime une réservation
        pre:
            - id: L'identifiant de la réservation
        Exemple : supprimer_reservation 1
                post: Supprime une réservation
        """
        self.get_data()
        for res in self.data["reservation_manager"]["reservations"]:
            if res["idRes"] == int(arg):
                self.data["reservation_manager"]["reservations"].remove(res)
        self.save_data()

    def do_exit(self, arg):
        """Quitte le programme"""
        print("Merci d'avoir utilisé le programme !")
        exit()

    def get_data(self):
        with open(self.file, "r") as file:
            file = file.read()
            file = json.loads(file)
            self.data = file

    def save_data(self):
        with open(self.file, "w") as file:
            file_data = json.dumps(self.data)
            file.write(file_data)
            print("Suppression faite !")

# Test
"""if __name__ == '__main__':
    ShellView().cmdloop()"""
