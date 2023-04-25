class Student :
    def __init__(self, nom, prenom, nbetudiant) :
        # Attribut privé pour stocker le nom de l'étudiant
        self.__nom = nom
        # Attribut privé pour stocker le prénom de l'étudiant
        self.__prenom = prenom
        # Attribut privé pour stocker le numéro d'étudiant de l'étudiant
        self.__nbetudiant = nbetudiant
        # Attribut privé pour stocker le nombre de crédits de l'étudiant (initialisé à 0)
        self.__nbcredits = 0
        # Attribut privé pour stocker le niveau de l'étudiant en utilisant la méthode privée __studentEval()
        self.__level = self.__studentEval()

    # Méthodes pour obtenir les informations de l'étudiant

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom
    
    def get_nbetudiant(self):
        return self.__nbetudiant
    
    # Méthodes pour mettre à jour les informations de l'étudiant

    def set_nom(self, new_nom):
        self.__nom = new_nom

    def set_prenom(self, new_prenom):
        self.__prenom = new_prenom

    def set_nbetudiant(self, new_nbetudiant):
        self.__nbetudiant = new_nbetudiant

     # Méthode pour ajouter des crédits à l'étudiant
    def add_credits(self, credits):
        if credits > 0:
            # Ajout du nombre de crédits spécifié à l'attribut nbcredits de l'étudiant
            self.__nbcredits += credits
        else:
            print("Le nombre de crédits ajouté doit être supérieur à zéro.")
        # Mise à jour de l'attribut level en utilisant la méthode privée __studentEval()
        self.__level = self.__studentEval()

    # Méthode pour obtenir le total des crédits de l'étudiant
    def get_total_credits(self):
        return self.__nbcredits

    # Méthode privée pour évaluer le niveau de l'étudiant
    def __studentEval(self):
        if self.__nbcredits >= 90:
            return "Excellent"
        elif self.__nbcredits >= 80:
            return "Très bien"
        elif self.__nbcredits >= 70:
            return "Bien"
        elif self.__nbcredits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    # Méthode pour afficher les informations de l'étudiant
    def studentInfo(self): 
        print("Nom :", self.__nom)
        print("Prénom :", self.__prenom)
        print("id :", self.__nbetudiant)
        print("Niveau :", self.__level)

# Instanciation de l'objet représentant l'étudiant John Doe avec les informations initiales
john_doe = Student("Doe", "John", 145)

# Ajout de crédits à trois reprises
john_doe.add_credits(36)
john_doe.add_credits(10)
john_doe.add_credits(24)

# Impression des informations de l'étudiant en console
john_doe.studentInfo()



        