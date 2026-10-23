#!/usr/bin/env python3
import sys

print('Bienvenue au Quiz pas ouf')


def start():
    print("Que voulez vous faire: ")
    print("1) Jouer ")
    print("2) Quitter")
    menu = input("Entrez votre reponse : ")
    if menu == "2":
        sys.exit("Arret du programme")
    else:
        print("Veuillez entrer un input valide")
        start()


start()

print('lancement')


class Score:
    pass
