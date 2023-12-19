from utils.classes.reservationManager import ReservationManager
from utils.classes.tableManager import TableManager
from utils.classes.type_cuisine_manager import type_cuisine_manager
from utils.classes.type_cuisine import	type_cuisine

def attribution(list, managerRes, managerTable, managerCuisine):
    '''
    Attribue une table à une reservation et vérifie si elle est libre ou pas.

    '''
    nomClient, numTel, dateHeure, idTypeCuisine, pmr, bb,nbr = list
    cuisine = managerCuisine.findCuisineById(idTypeCuisine)
    typeServ = cuisine.idService
    
    
    for table in managerTable.tables:
        if int(table.capaciteTable) >= int(nbr) and table.idService == typeServ:
            listeRes = managerRes.findReservationByTable(table.numTable)
            table_disponible = True
            for res in listeRes:
                if res.dateHeure == dateHeure:
                    table_disponible = False
                    break
            if table_disponible:
                list.append(table.numTable)
                return list
    return False
#commentaire