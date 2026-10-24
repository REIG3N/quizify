#!/usr/bin/env python3
import sys

from quiz import Quiz
from user import User
from utils import afficher_entete

# initialisation de la variable nom
nom = ""
while not nom:
    nom = input("Votre nom : ").strip()
user = User(nom)


def choisir_theme(themes):
    """
        choix du thu00e8mes du quiz parmi la liste
    """
#   la boucle de choix est lancer tant que la saisie est invalide
    while True:
        # affichage de l'entete via utils,
        # nettoyr l'affichage
        afficher_entete()
        print("Choisissez un thu00e8me :")
        # boucle pour afficher tout les thu00e8mes
        # permet d'en ajouter a l'avenir
        for i, theme in enumerate(themes, 1):
            print(f"{i}) {theme}")
        saisie = input("Entrez votre reponse : ").strip()
        if saisie.isdigit() and 1 <= int(saisie) <= len(themes):
            return themes[int(saisie) - 1]


def jouer():
    """
    Fonction jouer: active le quiz selon le thu00e8me choisi
    """
    # initialiasation et lien de la classe quiz et les donnu00e9es.
    quiz = Quiz("data/questions.json")
    # si ca charge pas on reste dans le menu
    if not quiz.charger():
        return
    # choix du theme
    theme = choisir_theme(quiz.themes())
    # selectionne uniquement les questions du thu00e8me
    quiz.filtrer(theme)
    quiz.jouer()
    # tableau de fin de partie
    quiz.resume()
    # on enregistre le score et le thu00e8me dans le profil du user
    user.ajouter_score(theme, quiz.score)


def menu():
    """
    fonction de navigation et d'affichage,
    affichage simple et compact avec affiche_entete.
    choix par chiffre similaire aux quizz
    """
    while True:
        afficher_entete()
        print("Que voulez vous faire: ")
        print("1) Jouer !!!")
        print("2) Voir resultats")
        print("3) Quitter le quiz")
        prompt = input("Entrez votre reponse : ").strip()
        if prompt == "1":
            jouer()
        elif prompt == "2":
            afficher_entete()
            user.afficher_resultats()
        elif prompt == "3":
            sys.exit("Arret du programme...")
        else:
            input(
                "Veuillez entrer un input valide, (Appuyer n'importe ou pour ressayer)")
            continue
        # input de retour vers le menu apru00e8s un quiz ou resultat.
        input("\nAppuyez sur Entree pour revenir au menu...")


menu()
