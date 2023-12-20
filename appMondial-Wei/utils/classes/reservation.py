"""No Import"""


class Reservation:
    """
    class used to init a new reservation for a restaurant
    """
    def __init__(self, nom: str, telNum, numTable, dateHeure, idCuisine, pmr=0, bb=0, nbrClient=1, idRes=1):
        """
        pre :
            -le nom doit être une chaine de caractère
            -le numéro de téléphone (telNum) doit être une chaine de caractère
            -le numéro de Table doit être un chiffre strictement plus grand que 0
            -l'identification du type cuisine doit être égale a eu , azy , af , an , VIP ou as
            -pmr doit être un chiffre plus grand ou égale a 0
            -bb doit être un chiffre plus grand ou égale a 0
            -le nombre de Client doit être un chiffre plus grand ou égal a 1
            -l'identification de la Reservation doit être un strictement plus grand que 0
        post : création d'une nouvelle instance Reservation
        """
        assert isinstance(nom, str), "le nom doit etre une chaine de charactères."
        assert isinstance(telNum, str), "Le numero de telephone doit être une chaine de caractère."
        assert isinstance(numTable, int) and numTable > 0, "La table doit est un chiffre strictement positif."
        assert isinstance(idCuisine, str) and idCuisine in ["eu", "azy", "af", "as", "an", "VIP"], \
            "L'id cuisine doit être égale a eu,az,af,an,as."
        assert isinstance(int(pmr), int) and int(pmr) >= 0, "Il faut indiquer le nombre de personne pmr."
        assert isinstance(int(bb), int) and int(bb) >= 0, "Il faut indiquer le nombre de bb."
        assert isinstance(idRes, int) and idRes >= 1, "il faut ajouter un id supperieur a 0."
        assert isinstance(int(nbrClient), int) and int(nbrClient) >= 1, "il faut metre un chifffre superieur a 1"
        self.__nom = nom
        self.__telNum = telNum
        self.__numTable = numTable
        self.__dateHeure = dateHeure
        self.__idCuisine = idCuisine
        self.__pmr = pmr
        self.__bb = bb
        self.__nbrClient = nbrClient
        self.__idRes = idRes

    def __str__(self):
        """
        pre : --
        post :retourne une representation textuel de la reservation
        """
        return (f"ID: {self.idRes} nom :{self.nom}, telNum :{self.telNum}, numTable :{self.numTable}"
                f", dateHeure :{self.dateHeure}, idCuisine :{self.idCuisine}, pmr :{self.pmr}, bb :{self.bb}"
                f", nombre de personne :{self.nbrClient}")
    """
    :rest == modification of attribut 
    """
    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self,  new_nom: str):
        """
        pre: --
        post: modification du nom de l'instance
            -raise TypeError si le new_nom n'est pas une chaine de caractère
        """
        if not isinstance(new_nom, str):
            raise TypeError("Le nom n'est pas une chaîne de caractères.")
        self.__nom = new_nom

    @property
    def idRes(self):
        return self.__idRes

    @idRes.setter
    def idRes(self, new_idRes):
        """
        pre: --
        post: modification de l'id de Reservation de l'instance
            - raise TypeError si new_id_res n'est pas un chiffre
            - raise ValueError si new_id_res n'est pas un chiffre strictement plus grand que 0
        """
        if not isinstance(new_idRes, int):
            raise TypeError("l'idRes doit etre un chiffre")
        if not (isinstance(new_idRes, int) and new_idRes > 0):
            raise ValueError("l'idRes doit être strictement plus grand que 0")
        self.__id_res = new_idRes

    @property
    def telNum(self):
        return self.__telNum

    @telNum.setter
    def telNum(self, new_telNum):
        """
        pre: --
        post: modification du numéro de téléphone de l'instance
            - raise TypeError si le numero de téléphone n'est pas une chaine de caractère
        """
        if not isinstance(new_telNum, str):
            raise TypeError("le numero de telephone doit être une chaine de caractère")
        self.__tel_num = new_telNum

    @property
    def numTable(self):
        return self.__numTable

    @numTable.setter
    def numTable(self, new_numTable):
        """
         pre: --
         post: modification du numéro de table de l'instance
            -raise TypeError si le numéro de table n'est pas un chiffre
            -raise ValueError si le numéro de table n'est pas un chiffre strictement plus grand que 0
        """
        if not isinstance(new_numTable, int):
            raise TypeError("le numTable doit être un chiffre")
        if not (isinstance(new_numTable, int) and new_numTable > 0):
            raise ValueError("le numTable doit être un chiffre strictement plus grand que 0")
        self.__numTable = new_numTable

    @property
    def nbrClient(self):
        return self.__nbrClient

    @nbrClient.setter
    def nbrClient(self, new_nbrClient):
        """
         pre: --
         post: modification du nombre de client de l'instance
            -raise TypeError si le nombre de client n'est pas un chiffre
            -raise ValueError si le nombre de client n'est pas un chiffre plus grand ou égal a 1
        """

        if not isinstance(new_nbrClient, int):
            raise TypeError("le nombre de client doit être un chiffre")
        if new_nbrClient < 1:
            raise ValueError("le nombre de client doit être un chiffre plus grand ou égal à 1")
        self.__nbrClient = new_nbrClient

    @property
    def dateHeure(self):
        return self.__dateHeure

    @dateHeure.setter
    def dateHeure(self, new_dateHeure):
        """
        pre: --
        post: modifie la date et heure de l'instance
        """
        self.__dateHeure = new_dateHeure

    @property
    def idCuisine(self):
        return self.__idCuisine

    @idCuisine.setter
    def idCuisine(self, new_idCuisine):
        """
        pre: --
        post: Modification de l'identification du type de cuisine de l'instance
            -raise TypeError si l' identification du type de cusine n'est pas une chaine de caractère
            -raise ValueError si l'id du type de cuisine n'est pas égal a eu, azy, af, VIP, an ou as
        """
        if not isinstance(new_idCuisine, str):
            raise TypeError("id du type de cuisine est une chaine de caractère")
        if new_idCuisine not in ["eu", "azy", "af", "as", "an", "VIP"]:
            raise ValueError("id du type de cuisine doit être égal à eu, azy, af, VIP, an ou as")
        self.__idCuisine = new_idCuisine

    @property
    def pmr(self):
        return self.__pmr

    @pmr.setter
    def pmr(self, new_pmr):
        """
        pre: --
        post: modification du nombre de pmr de l'instance
            -raise TypeError si le nombre de pmr n'est pas un chiffre
            -raise ValueError si le nombre de pmr n'est pas un chiffre plus grand ou égal à 0
        """
        if not isinstance(new_pmr, int):
            raise TypeError("les pmr doit être un chiffre.")
        if not (isinstance(new_pmr, int) and new_pmr >= 0):
            raise ValueError("les pmr doit être un chiffre plus grand ou égal à 0.")
        self.__pmr = new_pmr

    @property
    def bb(self):
        return self.__bb

    @bb.setter
    def bb(self, new_bb):
        """
         pre: --
         post: modification du nombre de bb de l'instance
            -raise TypeError si le nombre de bb n'est pas un chiffre
            -raise ValueError si le nombre de bb n'est pas un chiffre plus grand ou égal à 0
        """
        if not isinstance(new_bb, int):
            raise TypeError("bb doit etre un chiffre.")
        if not (isinstance(new_bb, int) and new_bb >= 0):
            raise ValueError("bb doit etre un chiffre plus grand ou egale à 0.")
        self.__bb = new_bb
    
    def to_json(self):
        """
            pre: --
            post: Convertir les attributs de l'instance en un dictionnaire JSON
        """
        keys = ["nom","telNum","numTable","dateHeure","idCuisine","pmr","bb","nbrClient","idRes"]
        values = [self.nom,self.telNum,self.numTable,self.dateHeure,self.idCuisine,self.pmr,self.bb,self.nbrClient,self.idRes]
        dico=map(lambda x,y: (x,y),keys,values)
        dico = dict(dico)

        return dico

    @classmethod
    def from_json(cls, data):
        """
            pre: --
            post: Créez une instance à partir d'un dictionnaire
                -raise TypeError si le data n'est pas un dictionnaire
        """
        if not isinstance(data, dict):
            raise TypeError("data doit être un dictionnaire")

        return cls(
            nom=data.get("nom"),
            telNum=data.get("telNum"),
            numTable=data.get("numTable"),
            dateHeure=data.get("dateHeure"),
            idCuisine=data.get("idCuisine"),
            pmr=data.get("pmr"),
            bb=data.get("bb"),
            nbrClient=data.get("nbrClient"),
            idRes=data.get("idRes")
        )

