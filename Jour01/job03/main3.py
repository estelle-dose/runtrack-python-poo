class Operation :
    def __init__(self, nombre1, nombre2) :
        # Initialise l'attribut 'nombre1' avec la valeur de 'nombre1' passé en argument
        self.nombre1 = nombre1
        # Initialise l'attribut 'nombre2' avec la valeur de 'nombre2' passé en argument
        self.nombre2 = nombre2

    def addition(self):
        # Effectue l'addition des valeurs de 'nombre1' et 'nombre2' pour l'objet actuel et imprime le résultat
        print(self.nombre1+self.nombre2)

# Crée une instance de la classe Operation avec 'nombre1' égal à 12 et 'nombre2' égal à 3        
operation = Operation(12, 3)
# Appelle la méthode 'addition' sur l'objet 'operation' pour effectuer l'addition des attributs 'nombre1' et 'nombre2' et imprimer le résultat
operation.addition()