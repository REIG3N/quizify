#!/usr/bin/env python3
import sys

from quiz import Quiz
from user import User
from utils import afficher_entete

nom = ""
while not nom:
    nom = input("Votre nom : ").strip()
user = User(nom)


def jouer():
    quiz = Quiz("data/questions.json")
    if quiz.charger():
        quiz.jouer()
        quiz.resume()
        user.ajouter_score(quiz.questions[0].theme, quiz.score)


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
