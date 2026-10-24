import json
import os
import random

from utils import afficher_entete


class Question:
    """
    affichage et statut de la question/correction
    """

    def __init__(self, id, theme, intitule, options, reponse):
        self.id = id
        self.theme = theme
        self.intitule = intitule
        self.options = options
        self.reponse = reponse

    def afficher(self):
        afficher_entete()
        print(f"\n{self.intitule}")
        # on charge chaque option via enumerate
        # ca permet de gerer des questions avec plus ou moins d'options
        for i, option in enumerate(self.options, 1):
            print(f"  {i})  {option}")

    def est_correcte(self, choix):
        return self.options[choix - 1] == self.reponse

    def afficher_correction(self, symbole):
        print(f"  {symbole} {self.intitule}")
        print(f"    ❯ {self.reponse}")


class Quiz:
    """
    Charger les questions dans la liste question
    puis ranger dans bonnes et mauvaise 
    """

    def __init__(self, chemin):
        self.chemin = chemin
        self.questions = []
        self.bonnes = []
        self.mauvaises = []

    def charger(self):
        """ chargement et gestions des erreurs
        """
        # Stopper le quiz si le fichier n'est pas trouvable
        if not os.path.isfile(self.chemin):
            print(f"Fichier introuvable : {self.chemin}")
            return False
        # Stopper si le json n'est pas du json validé
        with open(self.chemin, "r", encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print(f"Fichier JSON invalide : {self.chemin}")
                return False
        self.questions = []
        # remplissage de la question et ajout dans la liste
        for q in data:
            question = Question(q["id"], q['theme'],
                                q["question"], q["options"], q["reponse"])
            self.questions.append(question)
        return len(self.questions) > 0

    def demander_choix(self, question):
        while True:
            saisie = input('Votre reponse : ').strip()
            if not saisie.isdigit():
                print('Entrez un nombre')
                continue
            choix = int(saisie)
            if 1 <= choix <= len(question.options):
                return choix
            print(f"Entrez un nombre entre 1 et {len(question.options)}")

    def jouer(self):
        self.bonnes = []
        self.mauvaises = []
        # selection aléatoire dans la liste, 10 par quiz
        for question in random.sample(
                self.questions, min(10, len(self.questions))):
            question.afficher()
            choix = self.demander_choix(question)
            # ajout des questions dans leurs listes respectives
            if question.est_correcte(choix):
                self.bonnes.append(question)
            else:
                self.mauvaises.append(question)

    def themes(self):
        liste = []
        for question in self.questions:
            if question.theme not in liste:
                liste.append(question.theme)
        return liste

    def filtrer(self, theme):
        filtrees = []
        for question in self.questions:
            if question.theme == theme:
                filtrees.append(question)
        self.questions = filtrees

    @property
    def score(self):
        """
        on appelle property ici pour faire fonctionner score
        comme une variable. il est recalculer a chaque fois.
        ca permet au score de se mettre a jour.
        """
        total = len(self.bonnes) + len(self.mauvaises)
        if total == 0:
            return 0
        return round(len(self.bonnes) * 100 / total)

    def resume(self):
        afficher_entete()
        total = len(self.bonnes) + len(self.mauvaises)
        print(f"\nScore : {self.score}% ({len(self.bonnes)}/{total})")

        print(f"\nRéponses correctes ({len(self.bonnes)}) :")
        for q in self.bonnes:
            q.afficher_correction("✓")

        print(f"\nRéponses incorrectes ({len(self.mauvaises)}) :")
        for q in self.mauvaises:
            q.afficher_correction("✗")
