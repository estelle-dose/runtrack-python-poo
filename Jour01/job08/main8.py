class Livre :
    def __init__(self, titre, auteur, nbpages) :
        # Initialise l'attribut privé '__titre' avec la valeur passée en argument
        self.__titre = titre
        # Initialise l'attribut privé '__auteur' avec la valeur passée en argument
        self.__auteur = auteur
        # Initialise l'attribut privé '__nbpages' avec la valeur passée en argument
        self.__nbpages = nbpages
        # Attribut privé pour stocker l'état de disponibilité du livre (par défaut, True)
        self.__disponible = True

    def get_titre(self):
        # Retourne la valeur de l'attribut privé '__titre'
        return self.__titre

    def get_auteur(self):
        # Retourne la valeur de l'attribut privé '__auteur'
        return self.__auteur
    
    def get_nbpages(self):
        # Retourne la valeur de l'attribut privé '__nbpages'
        return self.__nbpages
  
    def set_titre(self, new_titre):
        # Modifie la valeur de l'attribut privé '__titre' avec la nouvelle valeur passée en argument
        self.__titre = new_titre

    def set_auteur(self, new_auteur):
        # Modifie la valeur de l'attribut privé '__auteur' avec la nouvelle valeur passée en argument
        self.__auteur = new_auteur

    def set_nbpages(self, new_nbpages):
        if isinstance(new_nbpages, int) and new_nbpages > 0:
            # Modifie la valeur de l'attribut privé '__nbpages' avec la nouvelle valeur passée en argument
            self.__nbpages = new_nbpages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

    def afficher_livre(self):
        # Affiche la valeur de l'attribut privé '__titre'
        print("Titre :", self.__titre)
        # Affiche la valeur de l'attribut privé '__auteur'
        print("Auteur :", self.__auteur)
        # Affiche la valeur de l'attribut privé '__nbpages'
        print("Nombre de pages :", self.__nbpages)

    def vérification(self):
        # Méthode pour vérifier l'état de disponibilité du livre
        return self.__disponible
    
    def emprunter(self):
        if self.__disponible:
            # Méthode pour emprunter le livre (met à jour l'attribut d'état de disponibilité)
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.__disponible:
            # Méthode pour rendre le livre (met à jour l'attribut d'état de disponibilité)
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté auparavant.")

livre1 = Livre("Vampyria America : Le tombeau des immortels", "Victor Dixen", 592)
# Affiche les détails du livre
livre1.afficher_livre()

# Affiche la disponibilité du livre
print("Disponibilité du livre :", livre1.vérification())

# Emprunte le livre
livre1.emprunter()
# Affiche la disponibilité du livre mise à jour
print("Disponibilité du livre :", livre1.vérification())

# Rend le livre
livre1.rendre()
# Affiche la disponibilité du livre mise à jour
print("Disponibilité du livre :", livre1.vérification())