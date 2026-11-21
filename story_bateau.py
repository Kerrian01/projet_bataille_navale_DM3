from bateau import Bateau

# User story "chevauchement"

# Jeu 1 : deux bateaux qui se chevauchent
b1 = Bateau(2, 3, longueur=3)
b2 = Bateau(1, 4, longueur=3, vertical=True)
print("Jeu 1 :", b1.chevauche(b2))   # True

# Jeu 2 : deux bateaux qui ne se chevauchent pas
b1 = Bateau(0, 0, longueur=2)
b2 = Bateau(1, 0, longueur=2)
print("Jeu 2 :", b1.chevauche(b2))   # False
