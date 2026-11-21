class Bateau:
    marque = "⛵"
    message_coule = "Un bateau est coulé !"

    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    def positions(self):
        if self.vertical:
            return [(self.ligne + i, self.colonne) for i in range(self.longueur)]
        return [(self.ligne, self.colonne + i) for i in range(self.longueur)]

    def chevauche(self, autre):
        return len(set(self.positions()) & set(autre.positions())) > 0

    def coule(self, grille, touche="x"):
        return all(grille.case(l, c) == touche for l, c in self.positions())


class PorteAvion(Bateau):
    marque = "🚢"
    message_coule = "Le porte-avions est coulé !"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 4, vertical)


class Croiseur(Bateau):
    marque = "⛴"
    message_coule = "Le croiseur est coulé !"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 3, vertical)


class Torpilleur(Bateau):
    marque = "🚣"
    message_coule = "Le torpilleur est coulé !"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)


class SousMarin(Bateau):
    marque = "🐟"
    message_coule = "Le sous-marin est coulé !"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)
