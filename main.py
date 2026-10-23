#!/usr/bin/env python3
import sys

from quiz import Quiz
from user import User
from utils import afficher_entete

nom = ""
while not nom:
    nom = input("Votre nom : ").strip()
user = User(nom)


def choisir_theme(themes):
    while True:
        afficher_entete()
        print("Choisissez un thème :")
        for i, theme in enumerate(themes, 1):
            print(f"{1}) {theme}")
        saisie = input("Entrez votre reponse : ").strip()
        if saisie.isdigit() and 1 <= int(saisie) <= len(themes):
            return themes[int(saisie) - 1]


def jouer():
    quiz = Quiz("data/questions.json")
    if not quiz.charger():
        return
    theme = choisir_theme(quiz.themes())
    quiz.filter(theme)
    quiz.jouer()
    quiz.resume()
    user.ajouter_score(theme, quiz.score)


def menu():
    while True:
        afficher_entete()
        print("Que voulez vous faire: ")
        print("1) Jouer !!!")
        print("2) Voir resultats")
        print("3) Quitter le quiz")
        prompt = input("Entrez votre reponse : ")
        if prompt == "1":
            jouer()
        elif prompt == "2":
            afficher_entete()
            user.afficher_resultats()
        elif prompt == "3":
            sys.exit("Arret du programme...")
        else:
            print("Veuillez entrer un input valide")
            menu()
        input("\nAppuyez sur Entree pour revenir au menu...")


menu()
