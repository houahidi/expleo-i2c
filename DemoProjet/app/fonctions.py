"Defintion des fonctions "

def moyenne( liste ):
    "calcul de la moyenne d'une liste"
    print("calculer la moyenne de : ", liste)
    somme = sum(liste) # calculer la somme des élèments de la liste
    taille = len(liste) # calculer le nombre de la liste
    resultat = somme / taille # caluler la moyenne
    return resultat  # fournir le resultat en sortie


def factoriel(n):
    """ calcul du factoriel"""
    if n == 1 :
        return 1
    else:
        return n * factoriel(n - 1)
