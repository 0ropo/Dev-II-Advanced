class TableManager:
    def __init__(self):
        '''
        Initialise un gestionnaire de tables avec une liste vide de tables.

        PRE : -
        POST : Crée une liste vide pour stocker les tables.
        '''
        self.tables = []

    def addTable(self, new_table):
        '''
        Ajoute une nouvelle table à la liste des tables.

        PRE : new_table doit être un objet de type Table.
        POST : Ajoute la nouvelle table à la liste des tables.
        '''
        self.tables.append(new_table)

    def removeTable(self, table):
        '''
        Supprime une table de la liste des tables.

        PRE : table doit être une table existante dans la liste.
        POST : Supprime la table spécifiée de la liste des tables.
        '''
        self.tables.remove(table)

    def findTableWithNumber(self, num):
        '''
        Recherche une table avec un numéro spécifique.

        PRE : num doit être un entier correspondant au numéro de table à rechercher.
        POST : Renvoie la table correspondant au numéro spécifié s'il en existe une.
        '''
        for i in self.tables:
            if i.numTable == num:
                return i

    def afficherTables(self):
        '''
        Affiche les informations sur les tables.

        PRE : -
        POST : Affiche les informations de chaque table dans la liste.
        '''
        for i in self.tables:
            print(i)
