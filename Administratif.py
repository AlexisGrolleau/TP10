from Employe import *

class Administratif(Employe):
    def __init__(self,nom,prenom,salaire,id,anneeEmbauche,nbJTravail,service):
        Employe.__init__(self,nom,prenom,salaire,id,anneeEmbauche,nbJTravail)
        self.__service = service

    def print(self):
        print(f"* [id={self._id}] Nom et prénom : {self._nom} {self._prenom}, Salaire = {self._salaire}, Statut : Administratif, Année d'embauche : {self._anneEmbauche}, Nombre de jour de travail : {self._nbJTravail}, Service : {self.__service}" ,end='')
