import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = []
        self.creer_paquet()

    def creer_paquet(self):
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        for couleur in couleurs:
            for valeur in valeurs:
                carte = Carte(valeur, couleur)
                self.paquet.append(carte)

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def distribuer_cartes(self, nb_cartes):
        cartes = []
        for i in range(nb_cartes):
            carte = self.paquet.pop()
            cartes.append(carte)
        return cartes

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []

    def recevoir_cartes(self, cartes):
        self.main.extend(cartes)

    def afficher_main(self):
        print(f"\nMain de {self.nom}:\n")
        for carte in self.main:
            print(f"{carte.valeur} de {carte.couleur}")

    def calculer_total_main(self):
        total = 0
        nb_as = 0
        for carte in self.main:
            if carte.valeur in ['Valet', 'Dame', 'Roi']:
                total += 10
            elif carte.valeur == 'As':
                nb_as += 1
            else:
                total += int(carte.valeur)
        for i in range(nb_as):
            if total + 11 <= 21:
                total += 11
            else:
                total += 1
        return total

class Croupier:
    def __init__(self):
        self.main = []

    def recevoir_cartes(self, cartes):
        self.main.extend(cartes)

    def afficher_main(self):
        print("\nMain du croupier:\n")
        print(f"{self.main[0].valeur} de {self.main[0].couleur}")
        print("Carte cachée\n")

    def calculer_total_main(self):
        total = 0
        nb_as = 0
        for carte in self.main:
            if carte.valeur in ['Valet', 'Dame', 'Roi']:
                total += 10
            elif carte.valeur == 'As':
                nb_as += 1
            else:
                total += int(carte.valeur)
        for i in range(nb_as):
            if total + 11 <= 21:
                total += 11
            else:
                total += 1
        return total

# Exemple d'utilisation du jeu Blackjack

# Création du jeu et mélange du paquet de cartes
jeu = Jeu()
jeu.melanger_paquet()

# Création du joueur et distribution de 2 cartes
joueur = Joueur("Joueur 1")
cartes_joueur = jeu.distribuer_cartes(2)
joueur.recevoir_cartes(cartes_joueur)
joueur.afficher_main()

# Création du croupier et distribution de 2 cartes
croupier = Croupier()
cartes_croupier = jeu.distribuer_cartes(2)
croupier.recevoir_cartes(cartes_croupier)
croupier.afficher_main()

#Boucle principale du jeu
while True:
    # Demande au joueur s'il souhaite prendre une carte supplémentaire ou passer
    choix = input("Voulez-vous prendre une carte supplémentaire ? (Oui/Non) ").lower()
    if choix == 'oui':
        cartes_joueur = jeu.distribuer_cartes(1)
        joueur.recevoir_cartes(cartes_joueur)
        joueur.afficher_main()
        total_joueur = joueur.calculer_total_main()
    if total_joueur > 21:
        print("Vous avez dépassé 21, vous avez perdu.")
        break
    elif choix == 'non':
        break
    else:
        print("\nVeuillez entrer 'Oui' ou 'Non'.")

#Le croupier prend des cartes jusqu'à avoir au moins 17 points
while croupier.calculer_total_main() < 17:
    cartes_croupier = jeu.distribuer_cartes(1)
    croupier.recevoir_cartes(cartes_croupier)

#Affichage des mains du joueur et du croupier
joueur.afficher_main()
croupier.afficher_main()

#Comparaison des totaux de points pour déterminer le gagnant
total_joueur = joueur.calculer_total_main()
total_croupier = croupier.calculer_total_main()

if total_joueur > 21:
    print("Vous avez dépassé 21, vous avez perdu.")
elif total_croupier > 21:
    print("Le croupier a dépassé 21, vous avez gagné.")
elif total_joueur > total_croupier:
    print("Vous avez gagné.")
elif total_joueur < total_croupier:
    print("Le croupier a gagné.")
else:
    print("Égalité.")