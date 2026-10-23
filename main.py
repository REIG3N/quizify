#!/usr/bin/env python3
import sys
import json
import os

from quiz import Quiz


def menu():
    os.system("clear")
    with open("data/title.txt", "r", encoding="utf-8") as f:
        print(f.read())
    print("Que voulez vous faire: ")
    print("1) Jouer ")
    print("2) Quitter")
    prompt = input("Entrez votre reponse : ")
    if prompt == "2":
        sys.exit("Arret du programme")
    if prompt == "1":
        print("C'est parti")
    else:
        print("Veuillez entrer un input valide")
        menu()


game_running = True
while game_running:
    menu()
    quiz = Quiz("data/questions.json")
    if quiz.charger():
        quiz.jouer()
        quiz.resume()
        input("\nAppuyez sur Entrée pour revenir au menu...")
