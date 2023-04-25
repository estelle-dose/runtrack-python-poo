class Animal :
    def __init__(self) :
        # Initialise l'attribut 'age' à 0 lorsqu'un nouvel objet de la classe Animal est créé
        self.age = 0
        # Initialise l'attribut 'prenom' à une chaîne vide lorsqu'un nouvel objet de la classe Animal est créé
        self.prenom = ""

    def vieillir(self):
        # Incrémente l'attribut 'age' de 1 à chaque appel de cette méthode sur un objet de la classe Animal
        self.age += 1

    def nommer(self, nom):
        # Affecte la valeur de 'nom' à l'attribut 'prenom' de l'objet sur lequel cette méthode est appelée
        self.prenom=nom

# Crée une instance de la classe Animal    
animal = Animal()
# Affiche la valeur de l'attribut 'age' de l'objet 'animal'
print("L'age de l'animal", animal.age, "ans")

# Appelle la méthode 'vieillir' sur l'objet 'animal' pour incrémenter son attribut 'age'
animal.vieillir()
# Affiche la nouvelle valeur de l'attribut 'age' de l'objet 'animal'
print("L'age de l'animal", animal.age, "ans")

# Appelle la méthode 'nommer' sur l'objet 'animal' pour lui attribuer un prénom
animal.nommer("Jun")
# Affiche la valeur de l'attribut 'prenom' de l'objet 'animal'
print("L'animal se nomme", animal.prenom)