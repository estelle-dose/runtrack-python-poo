class Operation :
    def __init__(self, nombre1, nombre2) :
        # Initialise l'attribut 'nombre1' avec la valeur de 'nombre1' passé en argument
        self.nombre1 = nombre1
        # Initialise l'attribut 'nombre2' avec la valeur de 'nombre2' passé en argument
        self.nombre2 = nombre2

    def show_infos(self):
        # Affiche la valeur de 'nombre1' pour l'objet actuel
        print("le nombre 1 est", self.nombre1)
        # Affiche la valeur de 'nombre2' pour l'objet actuel
        print("le nombre 2 est", self.nombre2)

# Crée une instance de la classe Operation avec 'nombre1' égal à 12 et 'nombre2' égal à 3        
operation = Operation(12, 3)
# Appelle la méthode 'show_infos' sur l'objet 'operation' pour afficher les valeurs des attributs 'nombre1' et 'nombre2'
operation.show_infos()