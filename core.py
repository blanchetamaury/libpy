import csv as csv

def clamp(value, min, max):
    """Borne value dans l'intervalle min et max.

    arg:
        value: nombre a borner.
        min: Borne inferieur, il doit etre inferieur a max.
        max: Borne superieur, il doit etre superieur a min.
    
    Return:
        Si value est dans l'intervalle alors il retourne value.
        Si value est inferieur a min alors il retourne min.
        Si value est superieur a max alors il retourne max.
    Raise:
        valueError: si min > max.
    """
    if value < min:
        return min
    elif value > max:
        return max
    else:
        return value

def import_csv(fichier):
    """Import un fichier en l'ouvrant et le lisant, et renvoie une liste de dictionnaires.
    Arg:
        fichier: le nom du fichier a lire(sans le .csv)
    Return:
        une liste ou chaque ligne est representer par un dict
        {nom_de_colonne: value}.
    """
    lecteur = csv.DictReader(open(fichier + '.csv', 'r'))
    return [dict(ligne) for ligne in lecteur]

def export_csv(source_file ,dest_file , order):
    """Copie un CSV en réordonnant/filtrant les colonnes.

    Args:
        source_file: Nom (sans .csv) du fichier d’entrée.
        dest_file:  Nom (sans .csv) du fichier de sortie.
        order:      Ordre désiré des colonnes (noms identiques au header).
    """
    with open(source_file + '.csv', 'r') as src:
        lecteur = csv.DictReader(src)
        with open(dest_file + '.csv', 'w', newline='') as fichier:
            dic = csv.DictWriter(fichier, fieldnames=order)
            dic.writeheader()
            for ligne in lecteur:
                dic.writerow(ligne)
