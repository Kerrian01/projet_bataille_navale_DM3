from grille import Grille


g = Grille(5, 8)                                   # 1. créer une grille 5x8
while True:
    print(g)                                       # 2. afficher la grille
    saisie = input("ligne colonne (q pour quitter) : ")   # 3. coordonnées
    if saisie == "q":
        break
    ligne, colonne = map(int, saisie.split())
    g.tirer(ligne, colonne)                        # 4. tirer                                              # 5. retour en 2
