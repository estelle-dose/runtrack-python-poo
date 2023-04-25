class Personne :
    def __init__(self, prenom, nom) :
        # Initialise l'attribut 'prenom' avec la valeur de 'prenom' passé en argument
        self.prenom = prenom
        # Initialise l'attribut 'nom' avec la valeur de 'nom' passé en argument
        self.nom = nom

    def SePresenter(self):
        # Affiche une phrase de présentation en utilisant les valeurs des attributs 'prenom' et 'nom' pour l'objet actuel
        print("Je suis", self.prenom, self.nom)

# Crée une instance de la classe Personne avec 'prenom' égal à "Estelle" et 'nom' égal à "Dose"        
personne1 = Personne("Estelle", "Dose")
# Crée une autre instance de la classe Personne avec 'prenom' égal à "Harmonie" et 'nom' égal à "Soma"
personne2 = Personne("Harmonie", "Soma")

# Appelle la méthode 'SePresenter' sur l'objet 'personne1' pour afficher une phrase de présentation avec les attributs 'prenom' et 'nom' de 'personne1'
personne1.SePresenter()
# Appelle la méthode 'SePresenter' sur l'objet 'personne2' pour afficher une phrase de présentation avec les attributs 'prenom' et 'nom' de 'personne2'
personne2.SePresenter()