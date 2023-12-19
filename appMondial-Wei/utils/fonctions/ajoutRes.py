from utils.classes.reservation import Reservation
from utils.classes.reservationManager import ReservationManager
def ajouterReservation(list, managerRes):
    '''
        Ajoute une réservation à l'attribut reservations d'un objet issu de la classe ReservationManager
        grâce à la méthode addReservation et affiche l'objet.

        pré: param list de tyoe list param managerRes qui prend un objet de la classe ReservationManager
        post: --
        '''
    listId=[0]
    for reserv in managerRes.reservations:
        if reserv.idRes not in listId:
            listId.append(reserv.idRes)
            listId=sorted(listId,key=lambda elem:elem)

    if len(listId)!=0:
        id = listId[len(listId)-1]+1
    else:
        id=1
    res = Reservation(list[0],list[1],list[7],list[2],list[3],list[4],list[5],list[6],id)
    managerRes.addReservation(res)



    print(f'La réservation a bien été ajoutée !')
    print(res)
