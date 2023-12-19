class TypeService:
    '''
    class used to init the type of the service in a resto
    '''

    def __init__(self,idService,nom,idEtage):
        '''
        pre:idService == V or B
            nom == VIP or basic
            idEtage == int and idEtage >= 0
        post:initialise l'instance
        '''
        assert isinstance(idService, str) and idService == "V" or idService == "B", "l'id qu'il faut entrer est soit V ou B."
        assert isinstance(nom,str) and nom == "VIP" or nom == "Basique", "le nom qu'il faut entrer est soit VIP ou basique."
        assert isinstance(idEtage,int) and idEtage >= 0 , "le numero de l'etage doit etre un nombre strictement superieur a 0."
        self.__idService = idService
        self.__nom = nom
        self.__idEtage = idEtage
    def __str__(self):
        '''
        pre: --
        post:retourner l'object de l'initialisation de l'instance.
        '''
        return f" idService: {self.__idService}, nom: {self.__nom}, idEtage: {self.__idEtage}"

    '''
    :rest: security and modify
    '''
    @property
    def idService(self):
        return self.__idService
    @idService.setter
    def idService(self, new_idService):
        '''
        pre: idService == V or B
        post: initialise un nouveau idService a l'instance
        '''
        try:
            if not (isinstance(new_idService, str) and new_idService == "V" or new_idService == "B"):
                raise ValueError("l'id qu'il faut entrer est soit V ou B.")
            self.__idService = new_idService
        except ValueError as e:
            print(e)
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, new_nom):
        '''
        pre: nom == VIP or basic
        post: initialise un nouveaux nom a l'instance
        '''
        try:
            if not (isinstance(new_nom, str) and new_nom == "V" or new_nom == "B"):
                raise ValueError("le nom qu'il faut entrer est soit VIP ou basic.")
            self.__nom = new_nom
        except ValueError as e:
            print(e)

    @property
    def idEtage(self):
        return self.__idEtage
    @idEtage.setter
    def idEtage(self, new_idEtage):
        '''
               pre: idEtage == int and idEtage >= 0
               post: initialise un nouveau idEtage de l'instance
               '''
        try:
            if not (isinstance(new_idEtage,int) and new_idEtage >= 0):
                raise ValueError("le numero de l'etage doit etre un nombre strictement superieur a 0.")
            self.__idEtage = new_idEtage
        except ValueError as e:
            print(e)
    
    def to_json(self):
        # Convertir les attributs du type de service en un dictionnaire JSON
        return {
            "idService": self.idService,
            "nom": self.nom,
            "idEtage": self.idEtage
        }

    @classmethod
    def from_json(cls, data):
        # Créez une instance de TypeService à partir d'un dictionnaire JSON
        return cls(
            idService=data.get("idService"),
            nom=data.get("nom"),
            idEtage=data.get("idEtage")
        )