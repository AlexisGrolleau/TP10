from Employe import *

class Ingenieur(Employe):
    def __init__(self,nom,prenom,salaire,id,anneeEmbauche,nbJTravail,nbJProjet,nbJGestion):
        Employe.__init__(self,nom,prenom,salaire,id,anneeEmbauche,nbJTravail)
        self._nbJProjet = nbJProjet
        self._nbJGestion = nbJGestion

    def print(self):
        pass
