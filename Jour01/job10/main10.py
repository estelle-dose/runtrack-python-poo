class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    # Assesseurs
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def is_en_marche(self):
        return self.__en_marche

    # Mutateurs
    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    # Méthodes
    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True

    def arreter(self):
        self.__en_marche = False

    # Méthodes privées
    def __verifier_plein(self):
        if self.__reservoir > 5:
            return True
        else:
            print("Le réservoir est presque vide, veuillez faire le plein!")
            return False
        
# Création d'un objet voiture
voiture1 = Voiture("Toyota", "Corolla", 2021, 10000)

# Accès aux attributs avec les assesseurs
print("Marque : ", voiture1.get__marque())
print("Modèle : ", voiture1.get__modele())
print("Année : ", voiture1.get__annee())
print("Kilométrage : ", voiture1.get__kilometrage())
print("En marche : ", voiture1.is_en_marche())

# Modification des attributs avec les mutateurs
voiture1.set_marque("Honda")
voiture1.set_modele("Civic")
voiture1.set_annee(2022)
voiture1.set_kilometrage(15000)

# Vérification des attributs modifiés avec les assesseurs
print("Marque : ", voiture1.get__marque())
print("Modèle : ", voiture1.get__modele())
print("Année : ", voiture1.get__annee())
print("Kilométrage : ", voiture1.get__kilometrage())

# Démarrage de la voiture
voiture1.demarrer()
print("En marche : ", voiture1.is_en_marche())

# Tentative de démarrage avec un réservoir presque vide
voiture1._reservoir = 3  # Pour simuler un réservoir presque vide
voiture1.demarrer()  # Affiche un message d'alerte

# Arrêt de la voiture
voiture1.arreter()
print("En marche : ", voiture1.is_en_marche())