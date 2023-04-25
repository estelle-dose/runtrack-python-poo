class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque :", self.marque)
        print("Modèle :", self.modele)
        print("Année :", self.annee)
        print("Prix :", self.prix)

    def demarrer(self):
        print("Attention, je roule.\n")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes :", self.portes, "\n")

    def demarrer(self):
        print("La voiture démarre avec un vrombissement du moteur.")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue=2):
        super().__init__(marque, modele, annee, prix)
        self.roue = roue

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de roues :", self.roue, "\n")

    def demarrer(self):
        print("La moto démarre avec un rugissement du moteur.\n:")


# Instanciation d'un objet Voiture
voiture = Voiture("Mercedes", "Classe A", 2020, 18500, 4)
# Appel de la méthode informationsVehicule() sur l'objet Voiture
voiture.informationsVehicule()

# Instanciation d'un objet Moto
moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
# Appel de la méthode informationsVehicule() sur l'objet Moto
moto.informationsVehicule()

# Appel à la méthode demarrer sur la voiture et la moto
voiture.demarrer()
moto.demarrer()