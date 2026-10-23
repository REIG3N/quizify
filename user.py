import json
import os
from datetime import datetime


class User:
    def __init__(self, nom, chemin="data/utilisateurs.json"):
        self.nom = nom
        self.chemin = chemin

    def lire(self):
        if not os.path.isfile(self.chemin) or os.path.getsize(self.chemin) == 0:
            return {}
        with open(self.chemin, 'r', encoding='utf-8') as f:
            return json.load(f)

    def ecrire(self, data):
        with open(self.chemin, 'w', encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)

    def ajouter_score(self, theme, score):
        data = self.lire()
        if self.nom not in data:
            data[self.nom] = {"scores": []}
        data[self.nom]["scores"].append({
            "theme": theme,
            "score": score,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        self.ecrire(data)

    @property
    def scores(self):
        data = self.lire()
        if self.nom not in data:
            return []
        return data[self.nom]["scores"]

    def afficher_resultats(self):
        if not self.scores:
            print(f"Aucun résultat pour {self.nom}.")
            return
        print(f"\nRésultats de {self.nom}: ")
        for s in self.scores:
            print(f" {s['date']} {s['theme']:<20} {s['score']}%")
