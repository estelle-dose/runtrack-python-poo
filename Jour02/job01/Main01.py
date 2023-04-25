class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("L'âge de la personne est : ", self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

# Définition de la classe Eleve qui hérite de Personne
class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai", self.age, "ans")


class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


# Instanciation d'un objet de la classe Personne
personne1 = Personne()
# Affichage de l'âge par défaut de la personne
personne1.afficherAge()

# Instanciation d'un objet de la classe Eleve
eleve1 = Eleve()
# Appel des méthodes de la classe Eleve
eleve1.allerEnCours()
eleve1.affichageAge()

# Instanciation d'un objet de la classe Professeur
professeur1 = Professeur("Mathématiques")
# Appel des méthodes de la classe Professeur
professeur1.enseigner()