from datetime import datetime
from utils.classes.type_cuisine_manager import type_cuisine_manager
from utils.classes.type_cuisine import type_cuisine
def verifRes(list,managerCuisine):
    nom = list[0].split(" ")

    for elem in nom:
        for lettre in elem:
            if not isinstance(str(lettre),str) or not str(lettre).isalpha():
                print("Mauvais format nom client")
                return False

    for chiffre in list[1].split(" "):

        if not str(chiffre).isnumeric():
            print(chiffre)
            print("Pas bon format de numéro de téléphone")
            return False


    try:
        if not datetime.strptime(list[2] ,'%Y-%m-%d %H:%M'):
            print("Mauvais format de date")
            return False
    except TypeError:
        print("Mauvais format de date")
        return False
    except ValueError:
        print("Mauvais format de date")
        return False

    list[2] = datetime.strptime(list[2] ,'%Y-%m-%d %H:%M')
    now = datetime.now()
    if list[2] < now:
        print('La date doit être dans le futur !!!')
        return False

    if not managerCuisine.findCuisineByid(str(list[3]).lower()):
        print("Veuillez entrer un type de cuisine valide !")
        return False
    list[3] = list[3].lower()
    if not str(list[4]).lower() in ["oui","non"]:
        print("Il y'a t'il des pmr ? Oui-Non")
        return False
    if str(list[4]).lower() =="oui":
        list[4] = True
    else:
        list[4] = False
    
    if not str(list[5]).lower() in ["oui","non"]:
        print("Il y'a t'il des bébé ? Oui-Non")
        return False
    if str(list[5]).lower() == "oui":
        list[5] = True
    else:
        list[5] = False
    return list
