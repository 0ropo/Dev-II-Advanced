from utils.classes.typeService import TypeService
class TypeServiceManager:
    def __init__(self):
        '''
        pre:--
        post:initialise un liste pour mettre des instance
        '''
        self.services = []
    def addService(self,new_service):
        '''
        :param object new_service: service
        :add a service in the liste
        pre: new_service == Object
        post: ajouter un service a liste
        '''
        assert isinstance(new_service,object)
        self.services.append(new_service)
    def removeService(self,service):
        '''
        :param object service: service
        :remove a service in the liste
        pre: entree une nouvelle instance
              service in self.services
        post: retrait des donnees dans la list de l'instance
        '''
        try:
            if not(isinstance(service, TypeService) and service in self.services):
                raise ValueError("L'Object n'est pas de la list existant. Indiquer un Object existant dans l'instance. ")
            self.services.remove(service)
        except ValueError as e:
            print(e)
    def findServiceById(self,idService):
        '''
        :param int idService: id
        :find a service in the liste
        pre:idService == V or B
        post: retourne l'instance qui a cett idService
        '''
        try:
            if not isinstance(idService, str):
                raise ValueError("La valeur donnée n'est V ou B.")
            for i in self.reservations:

                if i.idService == idService:
                    return i
        except ValueError as e:
            print(e)
        except:
            print("erreur car pas dedans.")
    def afficherServices(self):
        '''
        :print liste
        pre:--
        post: afficher la liste
        '''
        for i in self.services:
            print(i)

    def to_json(self):
        services_json = [services.to_json() for services in self.services]
        return {
            "services": services_json
        }
    @classmethod
    def from_json(cls, data):
        manager = cls()
        services_data = data.get("services", [])
        for services_data in services_data:
            services = TypeService.from_json(services_data)
            manager.addService(services)
        return manager