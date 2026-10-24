import os


def afficher_entete():
    """
    afficher et maintenir le titre et clear le terminal,
    pour un rendu visuel propre et plus de lisibilité.
    """
    os.system("clear")
    with open("data/title.txt", "r", encoding="utf-8") as f:
        print(f.read())
    # appel du titre en ascii art via un .txt
    # autopep8 modifie les caractères en python
