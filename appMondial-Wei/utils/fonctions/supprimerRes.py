from utils.classes.reservation import Reservation
from utils.classes.reservationManager import ReservationManager

def supprimerRes(id, managerRes):
    res = managerRes.findReservationById(int(id))
    managerRes.removeReservation(res)
    return managerRes