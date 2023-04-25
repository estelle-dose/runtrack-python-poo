class Forme:
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur

    def aire(self):
        return self.__largeur * self.__hauteur


# Instanciation d'un objet Rectangle
rectangle = Rectangle(5, 10)

# Appel de la méthode aire() sur l'objet Rectangle
print("Aire du rectangle :", rectangle.aire())