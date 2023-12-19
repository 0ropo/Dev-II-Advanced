from utils.classes.reservation import Reservation
from utils.classes.reservationManager import ReservationManager
from utils.classes.tableManager import TableManager
from utils.classes.table import Table
from utils.classes.typeServiceManager import TypeServiceManager
from utils.classes.typeService import TypeService
from utils.fonctions.initial import initial
from utils.fonctions.ajoutRes import ajouterReservation
from utils.fonctions.argParse import argParse
from utils.classes.type_cuisine_manager import type_cuisine_manager
from utils.classes.type_cuisine import type_cuisine
from utils.fonctions.attrib import attribution
from utils.fonctions.verifRes import verifRes
from utils.fonctions.supprimerRes import supprimerRes
import eel
import json

def main():
    eel.init("web")
    eel.start("index.html")

@eel.expose
def importJSON():
    with open("managers.json","r") as file:
        file = file.read()
        file = json.loads(file)
    return file

@eel.expose
def supprimerDuGUI(id):
    with open("managers.json","r") as file:
        file = file.read()
        file = json.loads(file)
        managerRes = file["reservation_manager"]["reservations"]
        for res in managerRes:
            if res["idRes"] == id:
                managerRes.remove(res)
    with open("managers.json","w") as final:
        file = json.dumps(file)
        final.write(file)
        print("Suppression faite !")




@eel.expose
def mainGUI():

    init = initial()
    # Utilisation des managers
    managerRes = init.reservation_manager
    managerTable = init.table_manager
    managerService = init.typeServManager
    managerCuisine = init.typeCuisineManager
    
    dataJS = eel.exportPython()()
    liste = argParse(managerRes,dataJS)

    if liste == False:
        managerRes.affichage()
        return 0
    else:
        if liste[0] is False:
            managerRes.affichage()
            managerRes = liste[1]
            init.sauvegarder_managers()
            return 0
    if None in liste:
        print('python main.py -h')
        return 0


    liste = attribution(liste,managerRes,managerTable,managerCuisine)
    if liste is False:
        print("Désolé, il n'y a plus de place !")
        return 1
    #print(liste)
    ajouterReservation(liste,managerRes)

    init.sauvegarder_managers()

def dataBase():
    init = initial()

    # Utilisation des managers
    managerRes = init.reservation_manager
    managerTable = init.table_manager
    managerService = init.typeServManager
    managerCuisine = init.typeCuisineManager



    serv1= TypeService('B','Basique',0)
    serv2 = TypeService('V', 'VIP', 1)
    managerService.addService(serv2)
    managerService.addService(serv1)
    managerService.afficherServices()


    for i in range(26):
        table = Table(i+1, 4,'B')
        managerTable.addTable(table)
    table15 = Table(27, 15, 'B')
    managerTable.addTable(table15)
    for i in range(4):
        tableVip = Table(i+28,4,'V')
        managerTable.addTable(tableVip)

    managerTable.afficherTables()
    eu= type_cuisine('eu','Europe','B')
    azi = type_cuisine('azy', 'Asie', 'B')
    ads = type_cuisine('as', 'Amérique du Sud', 'B')
    adn = type_cuisine('an', 'Amérique du Nord', 'B')
    afri = type_cuisine('af', 'Afrique', 'B')
    vip = type_cuisine('vip', 'VIP', 'V')
    managerCuisine.addCuisine(eu,azi,ads,adn,afri,vip)
    managerCuisine.displayList()

    init.sauvegarder_managers()



def afficherManager():
    '''
    Affiche les services, les types de cuisine et les tables
    pré: --
    post: --
    '''
    init = initial()

    # Utilisation des managers
    managerRes = init.reservation_manager
    managerTable = init.table_manager
    managerService = init.typeServManager
    managerCuisine = init.typeCuisineManager

    managerService.afficherServices()
    managerCuisine.displayList()
    managerTable.afficherTables()


if __name__ == '__main__':
    main()