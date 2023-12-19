from utils.classes.type_cuisine import type_cuisine
class type_cuisine_manager:
    '''
    Classe utilisée pour initialiser une liste de différents types de cuisine.
    '''

    def __init__(self):
        '''
        Initialise une liste vide de types de cuisine.

        PRE : -
        POST : Crée une liste vide pour stocker les types de cuisine.
        '''
        self._cuisine_list = []

    '''
    :rest: sécurité et modification des attributs
    '''

    @property
    def cuisine_list(self):
        '''
        Récupère la liste des types de cuisine.

        PRE : -
        POST : Renvoie la liste des types de cuisine.
        '''
        return self._cuisine_list

    @cuisine_list.setter
    def cuisine_list(self, value):
        '''
        Définit une nouvelle liste de types de cuisine.

        PRE : value doit être une liste.
        POST : Remplace la liste actuelle par la nouvelle liste spécifiée.
        '''
        if isinstance(value, list):
            self._cuisine_list = value

    '''
    Méthodes utilisées pour ajouter, supprimer et afficher une cuisine de la liste.
    '''

    def addCuisine(self, *newCuisine):
        '''
        Ajoute des types de cuisine à la liste.

        PRE : newCuisine à ajouter
        POST : Ajoute les réservations à la liste des types de cuisine.

        Raise : newCuisine doit être un/des objets de type TypeCuisine non présents dans la liste.
        '''
        assert not isinstance(newCuisine, type_cuisine), "l'instance ne fait pas partie de type_cuisine"
        for cuisine in newCuisine:
            if cuisine not in self.cuisine_list:
                self.cuisine_list.append(cuisine)

    def removeCuisine(self, reservations):
        '''
        Supprime des types de cuisine de la liste.

        PRE : Les réservations à supprimer
        POST : Supprime les réservations de la liste des types de cuisine.

        Raise : Les réservations doivent être des objets de type TypeCuisine présents dans la liste.
        '''
        if not isinstance(reservations, type_cuisine):
            raise ValueError("l'instance a retirer n'est pas une instance de type_cuisine.")
        if not reservations in self._cuisine_list: 
            raise ValueError("l'instance a retirer n'est pas dans la liste des type_cuisine.")
        self._cuisine_list.remove(reservations)
        

    def displayList(self):
        '''
        Affiche la liste des types de cuisine.

        PRE : -
        POST : Affiche les informations de chaque type de cuisine dans la liste.
        '''
        if len(self.cuisine_list):
            print("Voici les éléments de la liste")
            for elem in self.cuisine_list:
                print(f"{elem}")

    def findCuisineById(self, id):
        '''
        Recherche un type de cuisine par son identifiant.

        PRE : id
        POST : Renvoie le type de cuisine correspondant à l'identifiant spécifié s'il existe.

        Raise : id doit être une chaîne de caractères correspondant à un identifiant de type de cuisine.
        '''
        
        if not isinstance(id,str):
            raise TypeError("ce n'est pas un str")
        for i in self.cuisine_list:
            if i.idCuisine == id:
                return i

    def __str__(self):
        '''
        Renvoie une représentation textuelle de la liste de cuisine.

        PRE : -
        POST : Renvoie une chaîne de caractères contenant la liste des types de cuisine.
        '''
        return f"Liste de cuisine : {self._cuisine_list}"

    def to_json(self):
        cuisine_list_json = [cuisine_list.to_json() for cuisine_list in self.cuisine_list]
        return {
            "cuisine_list": cuisine_list_json
        }

    @classmethod
    def from_json(cls, data):
        manager = cls()
        cuisine_list_data = data.get("cuisine_list", [])
        for cuisine_list_data in cuisine_list_data:
            cuisine_list = type_cuisine.from_json(cuisine_list_data)
            manager.addCuisine(cuisine_list)
        return manager