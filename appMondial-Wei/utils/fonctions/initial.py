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