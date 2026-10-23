import os


def afficher_entete():
    os.system("clear")
    with open("data/title.txt", "r", encoding="utf-8") as f:
        print(f.read())
