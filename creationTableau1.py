import numpy as np
def creationTableau1(liste:list):
    """Creer un tableau numpy unidimensionnel composé des elements de la liste en argument multiplié par 2
    method:
        utiliser les fonctions integres dans la librairie numpy (np.array)
    Args:
        liste (list): la liste de nombres entiers
    sorties:
        tableau (numpy.array): le tableau numpy contenant les elements de la lise multipliés par 2
    """
    return np.array([i * 2 for i in liste])