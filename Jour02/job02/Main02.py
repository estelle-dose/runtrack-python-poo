class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("L'âge de la personne est :", self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
        self.age = age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai", self.age, "ans")


class Professeur(Personne):
    def __init__(self, age, matiereEnseignee):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


# Instanciation d'un objet Personne avec l'âge par défaut de 14 ans
personne = Personne()
# Instanciation d'un objet Eleve avec l'âge par défaut de 14 ans
eleve = Eleve()
# Affichage de l'âge de l'élève après la modification à 15 ans
eleve.modifierAge(15)
eleve.afficherAge()

# Appel des méthodes bonjour() et allerEnCours() sur l'objet Eleve
eleve.bonjour()
eleve.allerEnCours()

# Instanciation d'un objet Professeur avec l'âge de 40 ans et la matière enseignée "Mathématiques"
professeur = Professeur(40, "Mathématiques")

# Appel des méthodes bonjour() et enseigner() sur l'objet Professeur
professeur.bonjour()
professeur.enseigner()