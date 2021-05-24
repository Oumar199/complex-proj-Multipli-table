from random import seed, randint
def creationListe():
    """Cette fonction permet de créer une liste de 30 nombres entiers pris aléatoirement situés entre 0 et 50
    method : 
        Utiliser la librairie numpy 
    besoins :
        None
    Sorties :
        Le tableau numpy
    """
    seed(0)
    return [randint(0, 50) for i in range(30)]

