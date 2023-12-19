class Table:
    '''
    class used for init a new table
    '''
    def __init__(self,numTable,capaciteTable,idService):
        '''
        pre: numTable == int and numTable > 0
             capaciteTable == 2 ,4 ,15 and int
             idService == str and idService == VIP, basic
        post: initialisation de l'instance Table
        '''
        assert isinstance(numTable, int) and numTable > 0, "L'id de la table doit être un nombre strictement positif."
        assert isinstance(capaciteTable, int) and capaciteTable == 2 or capaciteTable == 4 or capaciteTable == 15, "le nombre de personne autoriser sur une table sont 2,4,15."
        assert isinstance(idService, str) and idService == "V" or idService == "B", "l'id qu'il faut entrer est soit V ou B."
        self.__numTable = int(numTable)
        self.__capaciteTable = int(capaciteTable)
        self.__idService = idService

    def __str__(self):
        '''
        pre:--
        post:retourne le dictionnaire de initialisation de Table
        '''
        return f"numTable: {self.__numTable}, capaciteTable: {self.__capaciteTable}, idService: {self.__idService} "

    '''
    :rest: modify and security
    '''
    @property
    def numTable(self):
        return self.__numTable
    @numTable.setter
    def numTable(self, new_numTable):
        '''
        pre: new_numTable == int and new_numTable > 0
        post: ajouter une nouvelle table a l'instance
        '''
        try:
            if not isinstance(new_numTable, int):
                raise TypeError("L'id de la table doit être un nombre.")
            if not (isinstance(new_numTable, int) and new_numTable > 0):
                raise ValueError("L'id de la table doit être un nombre strictement plus grand que 0.")
            self.__numTable = new_numTable
        except (ValueError, TypeError) as e:
            print(e)

    @property
    def capaciteTable(self):
        return self.__capaciteTable
    @capaciteTable.setter
    def capaciteTable(self, new_capaciteTable):
        '''
        pre: new_capaciteTable == 2 ,4 ,15 and int
        post: ajouter un noouveau nombre de personnne a une table dans l'instance
        '''
        try:

            if not isinstance(new_capaciteTable, int) :
                raise TypeError("le nombre de personne doit être un nombre.")
            if not (isinstance(new_capaciteTable, int) and new_capaciteTable == 2 or new_capaciteTable == 4 or new_capaciteTable == 15):
                raise ValueError("le nombre de personne autoriser sur une table sont 2,4,15.")
            self.__capaciteTable = new_capaciteTable
        except (ValueError,TypeError) as e :
            print(e)

    @property
    def idService(self):
        return self.__idService
    @idService.setter
    def idService(self, new_idService):
        '''
            pre: new_idService == str and new_idService == VIP, basic
            post: ajouter un nouveau new_idService a l'intsance
        '''
        try:
            if not (isinstance(new_idService, str) and new_idService == "V" or new_idService ==  "B"):
                raise ValueError("l'id qu'il faut entrer est soit V ou B.")
            self.__idService = new_idService
        except ValueError as e:
            print(e)
    def to_json(self):
        # Convertir les attributs de la table en un dictionnaire JSON
        return {
            "numTable": self.numTable,
            "capaciteTable": self.capaciteTable,
            "idService": self.idService
        }

    @classmethod
    def from_json(cls, data):
        # Créez une instance de la table à partir d'un dictionnaire JSON
        return cls(
            numTable=data.get("numTable"),
            capaciteTable=data.get("capaciteTable"),
            idService=data.get("idService")
        )