class Rectangle :
    def __init__(self, longueur, largeur) :
        # Initialise l'attribut privé '__longueur' avec la valeur passée en argument
        self.__longueur = longueur
        # Initialise l'attribut privé '__largeur' avec la valeur passée en argument
        self.__largeur = largeur

    def get_longueur(self):
        # Retourne la valeur de l'attribut privé '__longueur'
        return self.__longueur

    def get_largeur(self):
        # Retourne la valeur de l'attribut privé '__largeur'
        return self.__largeur

    def set_longueur(self, nouvelle_longueur):
        # Modifie la valeur de l'attribut privé '__longueur' avec la nouvelle valeur passée en argument
        self.__longueur = nouvelle_longueur

    def set_largeur(self, nouvelle_largeur):
        # Modifie la valeur de l'attribut privé '__largeur' avec la nouvelle valeur passée en argument
        self.__largeur = nouvelle_largeur

# Crée une instance de la classe Rectangle avec les valeurs 10 pour 'longueur' et 5 pour 'largeur'
rectangle = Rectangle(10, 5)
# Affiche les valeurs des attributs 'longueur' et 'largeur' de l'objet 'rectangle'
print("longueur :", rectangle.get_longueur(), "largeur :", rectangle.get_largeur())

# Appelle la méthode 'set_longueur' pour modifier la valeur de 'longueur' de l'objet 'rectangle'
rectangle.set_longueur(11)
# Appelle la méthode 'set_largeur' pour modifier la valeur de 'largeur' de l'objet 'rectangle'
rectangle.set_largeur(6)
# Affiche les nouvelles valeurs des attributs 'longueur' et 'largeur' de l'objet 'rectangle'
print("longueur modifiée :", rectangle.get_longueur(), "largeur modifiée :", rectangle.get_largeur())
