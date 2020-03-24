class Multinational:
    def __init__(self,nom,paysOrigine):
        self.__nom = nom
        self.__paysOrigine = paysOrigine
        self.__filiale = []

    def ajouterFiliale(self,filiale):
        self.__filiale.append(filiale)

    def print(self):
        print(10*"-")
        print(f"La multinationale {self.__nom} est composé de {len(self.__filiale)} filiales. Son pays d'origine est : {self.__paysOrigine}.")

        creaini = 5000
        nom = ""
        nombresalarie = 0
        for i in self.__filiale:
            if i._dateCreation < creaini:
                creaini = i._dateCreation
                nom = i._nom
                nombresalarie = len(i._salarie)
        print(f"La filiale la plus ancienne de cette multinationale est : {nom}. Elle est composé de {nombresalarie} salariés.")

        nbsalarie = 0
        for i in self.__filiale:
            nbsalarie += len(i._salarie)
        print(f"{self.__nom} est composé de {nbsalarie} salariés :")

        for i in self.__filiale:
            i.print()

        print(10*"-")


