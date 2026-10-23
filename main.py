#!/usr/bin/env python3
import sys
import json

from quiz import Quiz

print('Bienvenue au Quiz pas ouf')


def menu():
    print("Que voulez vous faire: ")
    print("1) Jouer ")
    print("2) Quitter")
    menu = input("Entrez votre reponse : ")
    if menu == "2":
        sys.exit("Arret du programme")
    if menu == "1":
        print("C'est parti")
    else:
        print("Veuillez entrer un input valide")
        menu()


menu()

quiz = Quiz("data/questions.json")
if quiz.charger():
    quiz.jouer()
    quiz.resume()


menu()
