from utils.classes.reservation import Reservation
from utils.classes.reservationManager import ReservationManager
def ajouterReservation(list, managerRes):
    '''
    Ajoute une réservation à l'attribut reservations d'un objet issu de la classe ReservationManager
    grâce à la méthode addReservation et affiche l'objet.

    pré: param list de tyoe list param managerRes qui prend un objet de la classe ReservationManager
    post: --
    '''
    res = Reservation(list[0],list[1],list[2],list[3],list[4],list[5])
    managerRes.addReservation(res)
    print(managerRes)


import argparse


def argParse():
    '''
    Permet de prendre la reservation en ligne de commande en entrant divers paramètres.

    pré: --
    post: Si args.affichage == True alors il retourne False,
          sinon il retourne une liste contenant les données passées en argument.
    '''
    parser = argparse.ArgumentParser(
        description="Entrez les détails de la réservation. out les champs d'information sont obligatoires sauf bb et pmr qui sont par défault sur non, -h (help) et -a (affiche) sont à utiliser seuls. Exemple: python main.py -nom 'John Doe' -tel 123456789 -dh '2023-10-10 19:00' -TC EU -pmr oui -bb non"
                    )

    parser.add_argument("-a", "--affichage", action="store_true", help="Affichage des réservations")
    parser.add_argument("-nom", type=str, help="Nom du client. Exemple: 'John Doe'")
    parser.add_argument("-tel", type=int, help="Numéro de téléphone. Exemple: 123456789")
    parser.add_argument("-dh", type=str,help="Date et heure de la réservation (format AAAA-MM-JJ HH:MM). Exemple: '2023-10-10 19:00' Vous devez mettre cette date entre '' ou guillemet. ")
    parser.add_argument("-nbr", type=int,
                        help="Nombre de personne : -nbr 15 ")

    parser.add_argument("-TC", type=str, help="ID du type de cuisine. Choix : Europe(eu), Asie (azy), Amérique du Nord/Sud (as/an), Afrique (af). Veuillez entrer l'id et non le nom complet.")
    parser.add_argument("-pmr", type=int,help="Nombre de personnes à mobilité réduite exemple: 1")
    parser.add_argument("-bb", type=int,help="Nombre de bébé(s) exemple: 2")


    args = parser.parse_args()
    assert isinstance(args.nom, str) or not str(args.nom).isalpha(), "Il faut que le nom soit écrit avec des charactères alphabétiques Exemple: Hugo"
    assert isinstance(args.tel,str) and str(args.tel).isnumeric(),"Il faut que le numéro de téléphone soit écrit avec des charactères numériques: 0468 78 33 99 "
    assert datetime.datetime.strptime(args.dh, '%Y-%m-%d %H:%M'),"La date et heure de la réservation (format AAAA-MM-JJ HH:MM). Exemple: '2023-10-10 19:00' Vous devez mettre cette date entre '' ou guillemet. "
    assert str(args.TC) in ["eu", "azy", "an", "as", "af","VIP"],"ID doit être du type de cuisine, les choix sont: Europe(eu), Asie (azy), Amérique du Nord/Sud (as/an), Afrique (af),VIP. Veuillez entrer l'id (PAS le nom complet.)"
    assert isinstance(args.pmr,int) and args.pmr >=0 ,"Le nombre de personne(s) à mobilité doit être un nombre positif entier"
    assert isinstance(args.nbr,int) and args.nbr >= 0,"Le nombre de personne(s) par table doit être un nombre entier positif ou 0"
    assert isinstance(args.bb,int) and args.bb >= 0,"Le nombre de bébé(s) par table doit être un nombre entier positif ou 0"
    if not args.affichage:
        return [args.nom,args.tel,args.dh,args.TC, args.pmr, args.bb,args.nbr]


from utils.classes.initialisation import Initialisateur

def initial():
    '''
    initial va chercher la sauvegarde et renvoie init qui contient tout les manager.
    pré: --
    post: --
    '''
    init = Initialisateur()
    init.charger_ou_initialiser_managers()
    return init


import datetime


def verifRes(list):
    '''
    Vérifie si les arguments rentrés en lignes de commandes correspondent au format demandé pour chaque élément et
    affiche le message d'erreur correspondant si ce n'est pas le cas.

    pré: le param list doit contenir des arguments de types str
    post: --
    '''
    nom = list[0].split(" ")
    for elem in nom:
        for lettre in elem:
            if not isinstance(str(lettre), str) or not str(lettre).isalpha():
                print("Mauvais format nom client")
                break
    for chiffre in list[1].split(" "):
        print(chiffre)
        if not str(chiffre).isnumeric():
            print("Pas bon format de numéro de téléphone")
    try:
        if not datetime.datetime.strptime(list[2], '%Y-%m-%d %H:%M'):
            print("mauvais format de date")
    except TypeError:
        print("Mauvais format de date")
    except ValueError:
        print("Mauvais format date")

    if not str(list[3]) in ["eu", "azy", "an", "as", "af"]:
        print("Print mauvais type de cuisine veuillez rentrer")

    if not str(list[4]).lower() in ["oui", "non"]:
        print("Il y'a t'il des pmr ? Oui-Non")
    # elif str(list[4]).lower() == "oui":
    # return True
    # else:
    # return False

    if not str(list[5]).lower() in ["oui", "non"]:
        print("Il y'a t'il des bébé ? Oui-Non")

    # if not int(list[6]) and int(list[6]) not in listTableId:
    # print("Numéro de table pas valide !")

