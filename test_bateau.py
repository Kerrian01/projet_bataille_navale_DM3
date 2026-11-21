from grille import Grille
from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin


def test_init_defaut():
    b = Bateau(2, 3)
    assert (b.ligne, b.colonne, b.longueur, b.vertical) == (2, 3, 1, False)


def test_positions():
    assert Bateau(2, 3, longueur=3).positions() == [(2, 3), (2, 4), (2, 5)]
    assert Bateau(2, 3, longueur=3, vertical=True).positions() == [(2, 3), (3, 3), (4, 3)]


def test_chevauche():
    assert Bateau(2, 3, longueur=3).chevauche(Bateau(1, 4, longueur=3, vertical=True))
    assert not Bateau(0, 0, longueur=2).chevauche(Bateau(1, 0, longueur=2))


def test_coule():
    g = Grille(3, 3)
    b = Bateau(1, 0, longueur=2)
    assert not b.coule(g)
    g.tirer(1, 0)
    assert not b.coule(g)
    g.tirer(1, 1)
    assert b.coule(g)


def test_sous_classes():
    assert PorteAvion(0, 0).longueur == 4
    assert Croiseur(0, 0).longueur == 3
    assert Torpilleur(0, 0).longueur == 2
    assert SousMarin(0, 0, True).vertical
    assert SousMarin(0, 0).marque == "🐟"
