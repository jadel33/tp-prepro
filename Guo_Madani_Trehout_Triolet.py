# Indiquez ici les NOMS, Prénoms des membres de l'équipe :
#   GUO Yue
#   MADANI Abdenour
#   TREHOUT Coline
#   TRIOLET Hugo


#------------------------------------------------------------------------------
#                               Extrait ensemble des voyelles


def extrait_ensemble_des_voyelles(mot):
    """ Fonction prenant en entrée un mot (chaîne de caratères)
        et renvoyant l'ensemble des voyelles minuscules présente
        dans celui-ci"""
    set_voyelle = set(["a", "e", "i", "u", "o", "y"])
    voyelles_mot = set()
    for s in mot:
        if s in set_voyelle:
            voyelles_mot.add(s)
    
    return voyelles_mot

    

#------------------------------------------------------------------------------
#                               Transforme en numéros


def transforme_en_numeros(mot):
    pass

#------------------------------------------------------------------------------
#                               JEU DE LA VIE


def contenu_cellule(colonne, ligne, univers):
    pass


def est_vivante(colonne, ligne, univers):
    pass


def largeur(univers):
    pass


def nombre_cases_vivantes_voisines(colonne, ligne, univers):
    pass


def prochain_univers(univers):
    pass

def iter_univers(univers):
    pass

#------------------------------------------------------------------------------
#                               TESTS : ne rien modifier dans ce qui suit
#------------------------------------------------------------------------------
if extrait_ensemble_des_voyelles("Toto le heros") != {"o", "e"}:
    print("Erreur de extrait_ensemble_des_voyelles('Toto le heros')")

if extrait_ensemble_des_voyelles("bcdE") != set():
    print("Erreur de extrait_ensemble_des_voyelles('bcd')")

if transforme_en_numeros("abz") != "1.2.26":
    print("Erreur de transforme_en_numeros('abz')")

if transforme_en_numeros("c") != "3":
    print("Erreur de transforme_en_numeros('c')")

def affiche_univers(univers):
    for ligne in univers:
        print(ligne)

univers_1 = [
    "____",
    "_**_",
    "_**_",
    "____"]

univers_2 = [
    "______",
    "______",
    "___*__",
    "_*_*__",
    "__**__",
    "______"]

if largeur(univers_1) != 4:
    print("Erreur de largeur(univers_1)")
if largeur(univers_2) != 6:
    print("Erreur de largeur(univers_2)")
if contenu_cellule(1, 1, univers_1) != "*":
    print("Erreur de contenu_cellule(1, 1, univers_1)")
if contenu_cellule(3, 3, univers_1) != "_":
    print("Erreur de contenu_cellule(3, 3, univers_1)")
if contenu_cellule(3, 1, univers_1) != "_":
    print("Erreur de contenu_cellule(3, 1, univers_1)")

if nombre_cases_vivantes_voisines(4, 0, univers_2) != 0:
    print("Erreur nombre_cases_vivantes_voisines(4, 0, univers_2)")

if nombre_cases_vivantes_voisines(2, 3, univers_2) != 5:
    print("Erreur nombre_cases_vivantes_voisines(2, 3, univers_2))")

univ_2 = univers_1
for _ in range(8):
    univ_2 = prochain_univers(univ_2)
if univ_2 != univers_1:
    print("Erreur prochain_univers")

it = iter_univers(univers_2)

liste_etats = []
for _ in range(7):
    univ_2 = next(it)
    liste_etats.append(univ_2)

for univ_2 in liste_etats:
    affiche_univers(univ_2)
    print("")
