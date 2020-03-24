from Ingenieur import *

class IngenieurJunior(Ingenieur):
    def __init__(self,nom,prenom,salaire,id,anneeEmbauche,nbJTravail,nbJProjet,nbJGestion,anneeExp):
        Ingenieur.__init__(self,nom,prenom,salaire,id,anneeEmbauche,nbJTravail,nbJProjet,nbJGestion)
        self.__anneeExp = anneeExp

    def print(self):
        print(f"* [id={self._id}] Nom et prénom : {self._nom} {self._prenom}, Salaire = {self._salaire}, Statut : Ingénieur-junior, Année d'embauche : {self._anneEmbauche}, Nombre de jour de travail : {self._nbJTravail}, Nombre d'heure de projet : {self._nbJProjet}, Nombre d'heure de Gestion : {self._nbJGestion}, Nombre d'années d'expérience : {self.__anneeExp}",end='')

class IngenieurSenior(Ingenieur):
    def __init__(self,nom,prenom,salaire,id,anneeEmbauche,nbJTravail,nbJProjet,nbJGestion,responsabilité):
        Ingenieur.__init__(self,nom,prenom,salaire,id,anneeEmbauche,nbJTravail,nbJProjet,nbJGestion)
        self.__responsabilité = responsabilité

    def print(self):
        print(f"* [id={self._id}] Nom et prénom : {self._nom} {self._prenom}, Salaire = {self._salaire}, Statut : Ingénieur-sénior, Année d'embauche : {self._anneEmbauche}, Nombre de jour de travail : {self._nbJTravail}, Nombre d'heure de projet : {self._nbJProjet}, Nombre d'heure de Gestion : {self._nbJGestion}, Responsabilité : {self.__responsabilité}",end='')

