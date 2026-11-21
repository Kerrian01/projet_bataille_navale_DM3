class Grille:
    def __init__(self, nombre_lignes, nombre_colonnes):
        self.vide = "∿"
        self.nombre_lignes = nombre_lignes
        self.nombre_colonnes = nombre_colonnes
        self.matrice = [self.vide] * (nombre_lignes * nombre_colonnes)

    def _indice(self, ligne, colonne):
        return ligne * self.nombre_colonnes + colonne

    def dans_la_grille(self, ligne, colonne):
        return 0 <= ligne < self.nombre_lignes and 0 <= colonne < self.nombre_colonnes

    def case(self, ligne, colonne):
        return self.matrice[self._indice(ligne, colonne)]

    def tirer(self, ligne, colonne, touche="x"):
        self.matrice[self._indice(ligne, colonne)] = touche

    def peut_ajouter(self, bateau):
        for ligne, colonne in bateau.positions():
            if not self.dans_la_grille(ligne, colonne):
                return False
            if self.case(ligne, colonne) != self.vide:
                return False
        return True

    def ajoute(self, bateau):
        if not self.peut_ajouter(bateau):
            return False
        for ligne, colonne in bateau.positions():
            self.matrice[self._indice(ligne, colonne)] = bateau.marque
        return True

    def __str__(self):
        lignes = []
        for l in range(self.nombre_lignes):
            debut = l * self.nombre_colonnes
            lignes.append("".join(self.matrice[debut:debut + self.nombre_colonnes]))
        return "\n".join(lignes)
