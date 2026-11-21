from grille import Grille
from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin


def test_init():
    g = Grille(5, 8)
    assert g.nombre_colonnes == 8
    assert len(g.matrice) == 40
    assert all(c == g.vide for c in g.matrice)


def test_tirer():
    g = Grille(5, 8)
    g.tirer(2, 3)
    assert g.matrice[2 * 8 + 3] == "x"
    g.tirer(0, 0, "💣")
    assert g.matrice[0] == "💣"


def test_str():
    g = Grille(5, 8)
    v = g.vide
    assert str(g) == "\n".join([v * 8] * 5)
    g.tirer(2, 3)
    assert str(g).split("\n")[2] == v * 3 + "x" + v * 4


def test_ajoute():
    g = Grille(2, 3)
    v = g.vide
    g.ajoute(Bateau(1, 0, longueur=2, vertical=False))
    assert g.matrice == [v, v, v, "⛵", "⛵", v]

    g = Grille(2, 3)
    g.ajoute(Bateau(1, 0, longueur=2, vertical=True))
    g.ajoute(Bateau(1, 0, longueur=4, vertical=True))
    assert g.matrice == [v] * 6


def test_ajoute_chevauchement():
    g = Grille(3, 3)
    assert g.ajoute(Bateau(0, 0, longueur=2))
    assert not g.ajoute(Bateau(0, 1, longueur=2))


def test_types_de_bateaux():
    g = Grille(8, 10)
    g.ajoute(PorteAvion(0, 0))
    g.ajoute(Croiseur(1, 0))
    g.ajoute(Torpilleur(2, 0))
    g.ajoute(SousMarin(3, 0))
    assert g.matrice[0:4] == ["🚢"] * 4
    assert g.matrice[10:13] == ["⛴"] * 3
    assert g.matrice[20:22] == ["🚣"] * 2
    assert g.matrice[30:32] == ["🐟"] * 2
