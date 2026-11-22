from grille import Grille
from bateau import Bateau, PorteAvion, Croiseur

g = Grille(5, 8)
g.ajoute(PorteAvion(0, 0))
g.ajoute(Croiseur(1, 2, vertical=True))
g.tirer(2, 3)
print(g)
