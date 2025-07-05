import csv as test

## def

def import_csv(fichier):
    lecteur = test.DictReader(open(fichier + '.csv', 'r'))
    return [dict(ligne) for ligne in lecteur]

def export_csv(lecteur_fichier,nom, ordre):
    with open(lecteur_fichier + '.csv', 'r') as src:
        lecteur = test.DictReader(src)
        with open(nom + '.csv', 'w', newline='') as fichier:
            dic = test.DictWriter(fichier, fieldnames=ordre)
            dic.writeheader()
            for ligne in lecteur:
                dic.writerow(ligne)

## main

tmp = import_csv('text')
print(tmp)

export_csv('text', 'ID', ['Sexe','Prénom','Année de naissance','ville'])