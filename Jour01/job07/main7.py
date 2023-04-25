class Livre :
    def __init__(self, titre, auteur, nbpages) :
        # Initialise l'attribut privé '__titre' avec la valeur passée en argument
        self.__titre = titre
        # Initialise l'attribut privé '__auteur' avec la valeur passée en argument
        self.__auteur = auteur
        # Initialise l'attribut privé '__nbpages' avec la valeur passée en argument
        self.__nbpages = nbpages

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

# Crée une instance de la classe Livre avec les valeurs spécifiées pour 'titre', 'auteur' et 'nbpages'
livre1 = Livre("Vampyria America : Le tombeau des immortels", "Victor Dixen", 592)
# Appelle la méthode 'afficher_livre' pour afficher les détails du livre
livre1.afficher_livre()

# Appelle la méthode 'set_titre' pour modifier la valeur de 'titre' de l'objet 'livre1'
livre1.set_titre("Vampyria America : Le tombeau des immortels (édition collector)")
# Appelle la méthode 'set_auteur' pour modifier la valeur de 'auteur' de l'objet 'livre1'
livre1.set_auteur("Victor Dixen (edition Collection R)")
# Appelle la méthode 'set_nbpages' pour modifier la valeur de 'nbpages' de l'objet 'livre1'
livre1.set_nbpages(624)
# Appelle la méthode 'afficher_livre' pour afficher les détails mis à jour du livre
livre1.afficher_livre()

# Appelle la méthode 'set_nbpages' avec une valeur non valide (nombre décimal) - affiche un message d'erreur
livre1.set_nbpages(50.5)






    