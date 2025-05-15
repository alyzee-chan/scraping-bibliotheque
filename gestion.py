# gestion_csv.py
import csv
import os

def charger_livres_csv():
    """Charge les livres depuis un fichier CSV s'il existe."""
    livres = []
    if os.path.exists("livres.csv"):
        with open("livres.csv", mode="r", encoding="utf-8") as fichier_csv:
            reader = csv.DictReader(fichier_csv)
            for row in reader:
                livres.append((row["Titre"], row["Prix"], row["Image URL"]))
    return livres

def sauvegarder_csv(livres_data):
    """Sauvegarde la liste des livres dans un fichier CSV."""
    with open("livres.csv", mode="w", newline="", encoding="utf-8") as fichier_csv:
        writer = csv.writer(fichier_csv)
        writer.writerow(["Titre", "Prix", "Image URL"])
        for livre in livres_data:
            writer.writerow(livre)