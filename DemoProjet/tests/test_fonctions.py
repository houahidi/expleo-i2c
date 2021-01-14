"tests des fonctions"

from app.fonctions import moyenne


def test():
    # jeu de donnees : une liste
    print("test moyenne")
    liste  = [1, 1 , 1]
    moyenne_attendu = 1
    resultat = moyenne(liste)
    print("comparaison : ", resultat == moyenne_attendu)

    assert resultat == moyenne_attendu


if __name__ == "__main__":
    # executer la fonction
    import nose2
    nose2.main()
