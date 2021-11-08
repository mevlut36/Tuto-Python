# le # permet de faire un commentaire
# --------------

# Importer une librairie
import math

# Quelques exemples de variables (syntaxe de la variable : |nom de la variable| = |texte, chiffre, liste...|

# Du texte (string en anglais)
ma_variable = "du texte"
# print() permet d'afficher du texte, un nombre une variable (ici la variable ma_variable)
print(ma_variable)

# des chiffres (int)
ma_variable_numero = 10
# affiche ma_variablee_numero pour valeur 10
print(ma_variable_numero)

# une liste (array)
ma_variable_liste = [10, 5, 8, 4, 9]

# affiche le contenu de ma (variable) liste pour valeur [10, 5, 8, 4, 9]
print(ma_variable_liste)


####### Niveau 2 ########

######### Les fonctions #########
# Créer une fonction, ici pour créer une fonction il faut commencer par "def" |nom que tu veux tout coller|
# ensuite dans les parenthese tu peux mettre des parametres comme le deuxieme exemple
def ma_fonction():
    # return permet de renvoyer une valeur, ici du texte on peut tres bien retourner avec une variable
    retourne = "Creation d'une fonction"
    return retourne
    # return "Creation d'une fonction"


# Exemple 2
# ici on donne en parametre la longueur et la largeur puis on fait retourne le resultat du calcul
def aire_rectangle(longueur, largeur):
    return "Resultat de l'aire du rectangle : ", longueur * largeur


# on utilise print pour appeler la fonction aire_rectangle
# puis on ajoute les parametres qu'on veut ici 5 et 2
print(aire_rectangle(5, 2))

######### Les boucles #########

# pour creer une boucle on utilise l'argument for puis une variable comme nb
# in range(5) permet de faire 5 tours de boucles (de 0 à 4)
for nb in range(5):
    print("Tour Num°", nb)


####### Niveau 3 ########

# pour creer une classe on commence avec l'argument class puis un nom, ici maClasse
class maClasse:
    # on initialise la classe, c'est un peu comme une fonction avec ses paramètres mais les paramètres sont dans une fonction nommé (obligatoirement) def __init__(self, param1, param2, ...):
    def __init__(self, nom, age, origine):
        self.nom = nom
        self.age = age
        self.origine = origine
        # pour utiliser les parametres on les renomme avec self.nom_de_variable

    # fonction tu connais
    def monNom(self):
        print(self.nom)

    def monAge(self):
        print(self.age)

    def monOrigine(self):
        print(self.origine)

    def afficheTout(self):
        print("Mon nom : ", self.nom, "| Mon age : ", self.age, "| Mon origine : ", self.origine)


# on creer une variable en appelant le nom de ma classe avec les parametres qu'on veut
var = maClasse("Mevlut", 18, "turc")

# maintenant qu'on appeler la classe maClasse on peut utiliser toute les fonctions qui sont dedans comme ci-dessous
var.monNom()
var.afficheTout()

# la suite une autre fois inshAllah zzzzzZZzzzzzZZzzzzZzzzzzz
