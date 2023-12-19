import argparse,datetime
from utils.fonctions.supprimerRes import supprimerRes
import eel



def argParse(managerRes,formData):
    '''
        Permet de prendre la reservation en ligne de commande en entrant divers arguments ou de supprimer une réservation.

        pré: managerRes est un objet issu de la classe ReservationManager
        post: Si args.affichage == True alors il retourne False,
              sinon il retourne une liste contenant les données passées en argument.
    '''
    parser = argparse.ArgumentParser(description="Entrez les détails de la réservation. Tout les champs d'information sont obligatoires sauf bb et pmr qui sont par défault sur non, -h (help) et -a (affiche) sont à utiliser seuls. Exemple: python main.py -nom 'John Doe' -tel 123456789 -dh '2023-10-10 19:00' -TC EU -pmr oui -bb non")

    parser.add_argument("-a", action="store_true", help="Affichage des réservations")
    parser.add_argument("-r", type=int, help="Supprimer une réservations des réservations : -r id ")
    parser.add_argument("-nom", type=str, help="Nom du client. Exemple: John Doe")
    parser.add_argument("-tel", type=str, help="Numéro de téléphone. Exemple: 123456789")
    parser.add_argument("-dh", type=str,help="Date et heure de la réservation (format AAAA-MM-JJ HH:MM). Exemple: \"2023-10-10 19:00\" Vous devez mettre cette date entre guillemet.")
    parser.add_argument("-nbr", type=int,help="Nombre de personne : -nbr 15 ")

    parser.add_argument("-TC", type=str, help="ID du type de cuisine. Choix : Europe(eu), Asie (azy), Amérique du Nord/Sud (as/an), Afrique (af), VIP (vip). Veuillez entrer l'id et non le nom complet.")
    parser.add_argument("-pmr", type=int, help="Nombre de personnes à mobilité réduite exemple: 1")
    parser.add_argument("-bb", type=int, help="Nombre de bébé(s) exemple: 2")


    args = parser.parse_args()
    args.nom = formData["nom"]
    args.tel = formData["tel"]
    args.nbr = formData["nbPers"]
    args.pmr = formData["nbPmr"]
    args.bb = formData["nbBb"]
    args.dh = formData["dateHeure"]
    args.TC = formData["typeCuisine"]


    if args.a:
        return False
    if args.r and managerRes:
        return False, supprimerRes(args.r, managerRes)
    else:

        assert isinstance(args.nom, str) or not str(
            args.nom).isalpha(), "Il faut que le nom soit écrit avec des charactères alphabétiques Exemple: Hugo"
        assert isinstance(args.tel, str) and str(
            args.tel).isnumeric(), "Il faut que le numéro de téléphone soit écrit avec des charactères numériques: 0468 78 33 99 "
        #assert datetime.datetime.strptime(args.dh,
         #                                 '%Y-%m-%d %H:%M'), "La date et heure de la réservation (format AAAA-MM-JJ HH:MM). Exemple: '2023-10-10 19:00' Vous devez mettre cette date entre '' ou guillemet. "
        assert str(args.TC) in ["eu", "azy", "an", "as", "af",
                                "VIP"], "ID doit être du type de cuisine, les choix sont: Europe(eu), Asie (azy), Amérique du Nord/Sud (as/an), Afrique (af),VIP. Veuillez entrer l'id (PAS le nom complet.)"
        assert isinstance(int(args.pmr), int) and int(
            args.pmr) >= 0 and int(args.pmr) + int(args.bb) <= int(args.nbr), "Le nombre de personne(s) à mobilité doit être un nombre positif entier et inférieur au nombre de personnes"
        assert isinstance(int(args.nbr), int) and int(
            args.nbr) >= 0, "Le nombre de personne(s) par table doit être un nombre entier positif ou 0"
        assert isinstance(int(args.bb), int) and int(
            args.bb) >= 0 and int(args.pmr) + int(args.bb) <= int(args.nbr), "Le nombre de bébé(s) par table doit être un nombre entier positif ou 0"

        return [args.nom,args.tel,args.dh,args.TC, args.pmr, args.bb,args.nbr]
