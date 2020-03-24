from Salarie import *

class Employe(Salarie):
    def __init__(self,nom,prenom,salaire,id,anneeEmbauche,nbJTravail):
        Salarie.__init__(self,nom,prenom,salaire,id)
        self._anneEmbauche = anneeEmbauche
        self._nbJTravail = nbJTravail

    def print(self):
        pass
