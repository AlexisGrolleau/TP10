from Salarie import *

class Directeur(Salarie):
    def __init__(self,nom,prenom,salaire,id,anneeNomi):
        Salarie.__init__(self,nom,prenom,salaire,id)
        self.__anneeNomi = anneeNomi

    def print(self):
        print(f"* [id={self._id}] Nom et prénom : {self._nom} {self._prenom}, Salaire = {self._salaire}, Statut: Directeur, Année de nomination : {self.__anneeNomi}",end='')
