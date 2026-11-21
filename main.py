import random
from termcolor import colored
from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

LIGNES = 8
COLONNES = 10
BOMBE = "💣"


def placer_bateaux(grille, classes):
    bateaux = []
    for classe in classes:
        possibilites = []
        for l in range(grille.nombre_lignes):
            for c in range(grille.nombre_colonnes):
                for vertical in (False, True):
                    b = classe(l, c, vertical)
                    if grille.peut_ajouter(b):
                        possibilites.append(b)
        bateau = random.choice(possibilites)
        grille.ajoute(bateau)
        bateaux.append(bateau)
    return bateaux


def afficher(grille):
    print(colored("   " + " ".join(str(c) for c in range(grille.nombre_colonnes)), "cyan"))
    for l in range(grille.nombre_lignes):
        ligne = []
        for c in range(grille.nombre_colonnes):
            case = grille.case(l, c)
            if case == grille.vide:
                ligne.append(colored(case, "blue"))
            elif case == "x":
                ligne.append(colored(case, "yellow"))
            elif case == BOMBE:
                ligne.append(colored(case, "red"))
            else:
                ligne.append(colored(case, "green"))
        print(colored(f"{l:2} ", "cyan") + " ".join(ligne))


def demander_tir(grille_visible):
    while True:
        saisie = input("Ligne et colonne (ex : 2 3) : ").split()
        try:
            ligne, colonne = int(saisie[0]), int(saisie[1])
        except (ValueError, IndexError):
            print(colored("Saisie invalide.", "red"))
            continue
        if not grille_visible.dans_la_grille(ligne, colonne):
            print(colored("En dehors de la grille.", "red"))
        elif grille_visible.case(ligne, colonne) != grille_visible.vide:
            print(colored("Case déjà jouée.", "red"))
        else:
            return ligne, colonne


def jouer():
    grille_bateaux = Grille(LIGNES, COLONNES)
    grille_visible = Grille(LIGNES, COLONNES)
    bateaux = placer_bateaux(grille_bateaux, [PorteAvion, Croiseur, Torpilleur, SousMarin])
    restants = list(bateaux)
    coups = 0

    while restants:
        afficher(grille_visible)
        ligne, colonne = demander_tir(grille_visible)
        coups += 1

        if grille_bateaux.case(ligne, colonne) == grille_bateaux.vide:
            grille_visible.tirer(ligne, colonne)
            print(colored("Plouf ! Dans l'eau.", "blue"))
            continue

        grille_visible.tirer(ligne, colonne, BOMBE)
        print(colored("Touché !", "red"))
        for bateau in restants:
            if bateau.coule(grille_visible, BOMBE):
                for l, c in bateau.positions():
                    grille_visible.tirer(l, c, bateau.marque)
                print(colored(bateau.message_coule, "green", attrs=["bold"]))
                restants.remove(bateau)
                break

    afficher(grille_visible)
    print(colored(f"Bravo ! Tous les bateaux sont coulés en {coups} coups.", "green", attrs=["bold"]))


if __name__ == "__main__":
    jouer()
