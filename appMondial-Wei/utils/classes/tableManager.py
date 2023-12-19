from utils.classes.table import Table


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

        PRE : new_table doit être un objet issu de la classe Table sinon une TypeError sera Raise
        POST : Ajoute la nouvelle table à la liste des tables.
        '''
        if not isinstance(new_table, Table):
            raise TypeError("La valeur ajouter n'est pas une instance de Table.")

        self.tables.append(new_table)

    def removeTable(self, table):
        '''
        Supprime une table de la liste des tables.

        PRE : table doit être issu de la classe table et faire partie de la liste table.
        POST : Supprime la table spécifiée de la liste des tables.

        '''

        if not isinstance(table, Table):
            raise ValueError("l'instance a retirer n'est pas une instance de Table.")
        if not table in self.tables:
            raise ValueError("l'instance a retirer n'est pas dans la liste des tables.")
        self.tables.remove(table)

    def findTableWithNumber(self, num):
        '''
        Recherche une table avec un numéro spécifique.

        PRE : num doit être un entier (int) correspondant au numéro de table à rechercher si il n'est pas entier alors une TypeError sera Raise
        POST : Renvoie la table correspondant au numéro spécifié s'il en existe une.
        '''
        if not isinstance(num, int):
            raise TypeError("La valeur donnée n'est pas un chiffre")
        for i in self.tables:
            if i.numTable == num:
                return i
        return None

    def afficherTables(self):
        '''
        Affiche les informations sur les tables.

        PRE : -
        POST :Affiche les informations de chaque table dans la liste. Les informations comprennent : numéro de table, capacité, état, etc.
        '''
        for i in self.tables:
            print(i)

    def to_json(self):
        """
            Convertit la liste des tables en une liste de dictionnaires JSON.

            PRE: -

            POST: Retourne un dictionnaire contenant une liste de tables converties en JSON.
            """

        tables_json = [table.to_json() for table in self.tables]
        return {
            "tables": tables_json
        }

    @classmethod
    def from_json(cls, data):
        '''
            Crée et retourne une instance de TableManager à partir d'un dictionnaire JSON.

            PRE : Le paramètre 'data' est un dictionnaire contenant des données JSON.
            POST : Crée une nouvelle instance de TableManager à partir des données JSON fournies.
            Les tables extraites des données sont ajoutées à l'instance de TableManager créée.
        '''
        manager = cls()
        tables_data = data.get("tables", [])
        for table_data in tables_data:
            table = Table.from_json(table_data)
            manager.addTable(table)
        return manager


tm = TableManager()
print(tm.tables == False)