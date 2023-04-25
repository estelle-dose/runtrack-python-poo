class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

    # Accesseurs
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.__hauteur * self.get_longueur() * self.get_largeur()

    # Accesseur
    def get_hauteur(self):
        return self.__hauteur

    # Mutateur
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur


# Instanciation d'un objet Rectangle
rectangle = Rectangle(5, 10)

# Appel des méthodes périmètre() et surface() sur l'objet Rectangle
print("Périmètre du rectangle :", rectangle.perimetre())
print("Surface du rectangle :", rectangle.surface())

# Utilisation des accesseurs pour obtenir les valeurs des attributs
print("Longueur du rectangle :", rectangle.get_longueur())
print("Largeur du rectangle :", rectangle.get_largeur())

# Utilisation des mutateurs pour modifier les valeurs des attributs
rectangle.set_longueur(8)
rectangle.set_largeur(12)

# Instanciation d'un objet Parallelepipede
parallelepiped = Parallelepipede(5, 10, 3)

# Appel des méthodes périmètre(), surface() et volume() sur l'objet Parallelepipede
print("Périmètre du parallélépipède :", parallelepiped.perimetre())
print("Surface du parallélépipède :", parallelepiped.surface())
print("Volume du parallélépipède :", parallelepiped.volume())

# Utilisation des accesseurs pour obtenir les valeurs des attributs
print("Longueur du parallélépipède :", parallelepiped.get_longueur())
print("Largeur du parallélépipède :", parallelepiped.get_largeur())
print("Hauteur du parallélépipède :", parallelepiped.get_hauteur())

# Utilisation des mutateurs pour modifier les valeurs des attributs
parallelepiped.set_longueur(8)
parallelepiped.set_largeur(12)
parallelepiped.set_hauteur(4)