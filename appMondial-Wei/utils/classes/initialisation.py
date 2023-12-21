from utils.classes.reservationManager import ReservationManager
from utils.classes.tableManager import TableManager
from utils.classes.typeServiceManager import TypeServiceManager
from utils.classes.type_cuisine_manager import type_cuisine_manager
import pickle
from pathlib import Path
import json
import re
import os

class Initialisateur:
    """
    Cette classe sert à initialiser et gérer les différents gestionnaires (managers) pour les réservations,
    les tables, les types de service, et les types de cuisine. Elle permet également de sauvegarder 
    et de charger ces gestionnaires depuis un fichier.

    Attributs:
        fichier_sauvegarde (str): Le nom du fichier de sauvegarde.
        reservation_manager (ReservationManager): Gestionnaire des réservations.
        table_manager (TableManager): Gestionnaire des tables.
        typeServManager (TypeServiceManager): Gestionnaire des types de service.
        typeCuisineManager (type_cuisine_manager): Gestionnaire des types de cuisine.
    """
    def __init__(self):
        fichier_sauvegarde_list = self.gen_backup_file()
        while True:
            try:
                fichier = next(fichier_sauvegarde_list)
                if os.path.exists(fichier) and os.path.isfile(fichier):
                    self.fichier_sauvegarde = fichier
                    break
            except StopIteration:
                self.fichier_sauvegarde = 'managers.json'
                break
        self.reservation_manager = None
        self.table_manager = None
        self.typeServManager = None
        self.typeCuisineManager = None

    def __str__(self):
        return f"ReservationManager avec {len(self.reservation_manager.reservations)} réservations"

    def initialiser_managers(self):
        """
        Initialise les gestionnaires avec de nouvelles instances.

        POST: 
        - Les gestionnaires de réservations, tables, types de service et types de cuisine sont initialisés.
        """
        self.reservation_manager = ReservationManager()
        self.table_manager = TableManager()
        self.typeServManager = TypeServiceManager()
        self.typeCuisineManager = type_cuisine_manager()

    def sauvegarder_managers(self):
        """
        Sauvegarde l'état actuel de tous les gestionnaires dans un fichier JSON.

        POST: 
        - L'état actuel de l'instance Initialisateur est sauvegardé dans un fichier JSON.
        """
        data = {
            "reservation_manager": self.reservation_manager.to_json(),
            "table_manager": self.table_manager.to_json(),
            "typeServManager": self.typeServManager.to_json(),
            "typeCuisineManager": self.typeCuisineManager.to_json()
        }

        with open(self.fichier_sauvegarde, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)




    def charger_ou_initialiser_managers(self):
        """
        Charge les gestionnaires à partir d'un fichier JSON de sauvegarde, ou les initialise si le fichier n'existe pas ou est corrompu.

        POST: 
        - Si le fichier de sauvegarde existe et est valide, les gestionnaires sont chargés à partir de ce fichier JSON.
        - Si le fichier n'existe pas ou est corrompu, les gestionnaires sont initialisés à nouveau.
        """
        try:
            if Path(self.fichier_sauvegarde).exists():
                with open(self.fichier_sauvegarde, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # print(data)
                    # Charger les gestionnaires à partir du dictionnaire JSON
                    self.reservation_manager = ReservationManager.from_json(data.get("reservation_manager", {}))
                    self.table_manager = TableManager.from_json(data.get("table_manager", {}))
                    self.typeServManager = TypeServiceManager.from_json(data.get("typeServManager", {}))
                    # print(self.typeServManager.services[1].idService)
                    self.typeCuisineManager = type_cuisine_manager.from_json(data.get("typeCuisineManager", {}))
                    # print(self.typeCuisineManager.cuisine_list)
            else:
                self.initialiser_managers()
        except (json.JSONDecodeError, FileNotFoundError):
            self.initialiser_managers()

    @staticmethod
    def get_fichier_sauvegarde(input_text):
        """
        :pre: input_text is a string to match with the regex pattern .*investigations_data.*\.bin
        :post: return the input_text if input_text matches the regex pattern else return None
        """
        pattern = re.compile(r".*managers.*\.json")
        return pattern.match(input_text)

    def gen_backup_file(self):
        """
        :post: yield the name of the backup_file if it exists
        """
        db_dir = './'
        for file in os.listdir(db_dir):
            if self.get_fichier_sauvegarde(file):
                yield f'{db_dir}/{file}'

