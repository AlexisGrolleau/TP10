from Multinational import *

class Filiale(Multinational):
    def __init__(self,nom,pays,dateCreation):
        self._nom = nom
        self._pays = pays
        self._dateCreation = dateCreation
        self._salarie = []

    def addSalarie(self,salarie):
        self._salarie.append(salarie)

    def delSalarie(self,salarie):
        self._salarie.remove(salarie)

    def print(self):
        for i in self._salarie:
            i.print()
            print(f", Site: {self._pays}")
