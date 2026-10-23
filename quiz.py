import json
import os
import random


class Question:
    def __init__(self, id, theme, intitule, options, reponse):
        self.id = id
        self.theme = theme
        self. intitule = intitule
        self.options = options
        self.reponse = reponse

    def afficher(self):
        print(f"\n{self.intitule}")
        for i, option in enumerate(self.options, 1):
            print(f"  {i})  {option}")

    def est_correcte(self, choix):
        return self.options[choix - 1] == self.reponse


class Quiz:
    def __init__(self, chemin):
        self.chemin = chemin
        self.questions = []
        self.bonnes = []
        self.mauvaises = []

    def charger(self):
        if not os.path.isfile(self.chemin):
            print(f"Fichier introuvable : {self.chemin}")
            return False
        with open(self.chemin, "r", encoding='utf-8') as f:
            data = json.load(f)

        self.questions = []
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
        for question in random.sample(
                self.questions, min(10, len(self.questions))):
            question.afficher()
            choix = self.demander_choix(question)
            if question.est_correcte(choix):
                self.bonnes.append(question)
            else:
                self.mauvaises.append(question)

    @property
    def score(self):
        total = len(self.bonnes) + len(self.mauvaises)
        if total == 0:
            return 0
        return round(len(self.bonnes) * 100 / total)

    def resume(self):
        print(
            f"\nScore: {self.score}% ({len(self.bonnes)}/{len(self.bonnes) + len(self.mauvaises)})")
        for q in self.mauvaises:
            print(f" x {q.intitule} -> {q.reponse}")
