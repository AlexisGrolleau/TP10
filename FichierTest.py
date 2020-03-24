import Administratif
import Directeur
import Filiale
import Multinational
import SousIngenieur


maMulti = Multinational.Multinational("RCAT","FRANCE")

FilTun = Filiale.Filiale("RCAT-Tunisie","Tunisie",2012)
FilBel = Filiale.Filiale("RCAT-Belgique","Belgique",2016)
FilMar = Filiale.Filiale("RCAT-Maroc","Maroc",2018)
FilAng = Filiale.Filiale("RCAT-Angleterre","Angleterre",2014)
maMulti.ajouterFiliale(FilTun)
maMulti.ajouterFiliale(FilBel)
maMulti.ajouterFiliale(FilMar)
maMulti.ajouterFiliale(FilAng)

directTuni = Directeur.Directeur("Jenner","Kylie",10,1452,2017)
FilTun.addSalarie(directTuni)

admiTuni = Administratif.Administratif("Muscu","Karim",8,1414,2015,50,"chomage")
IngeSeniorTuni = SousIngenieur.IngenieurSenior("Jenner","Kris",7,1450,2013,60,70,90,"Nucléaire")
FilTun.addSalarie(admiTuni)
FilTun.addSalarie(IngeSeniorTuni)

admiBelg = Administratif.Administratif("Elvis","Roméo",8,1454,2015,50,"Chocolat")
IngeJunBelg = SousIngenieur.IngenieurSenior("West","North",1,14504,2013,60,70,90,1)
FilBel.addSalarie(admiBelg)
FilBel.addSalarie(IngeJunBelg)

IngeSeniorMaroc = SousIngenieur.IngenieurSenior("LaSquale","Moha",7,14508,2013,60,70,90,"Détaille")
FilMar.addSalarie(IngeSeniorMaroc)

maMulti.print()

FilTun.delSalarie(admiTuni)
maMulti.print()

FilTun.delSalarie(IngeSeniorTuni)
FilBel.addSalarie(IngeSeniorTuni)

maMulti.print()
