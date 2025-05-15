


# interface.py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import io
import requests
from gestion_csv import charger_livres_csv
from affichage import afficher_livres
from scraping import scraper_livres
from gestion_csv import sauvegarder_csv

def creer_interface_principale(root):
    global entry_url, entry_recherche, frame_livres

    def lancer_scraping():
        url = entry_url.get()
        livres_data = scraper_livres(url)
        sauvegarder_csv(livres_data)
        afficher_livres(frame_livres, livres_data)

    def rechercher():
        mot = entry_recherche.get().lower()
        livres = charger_livres_csv()
        filtres = [livre for livre in livres if mot in livre[0].lower()]
        afficher_livres(frame_livres, filtres)

    frame_url = ttk.Frame(root)
    frame_url.pack(pady=5)

    entry_url = ttk.Entry(frame_url, width=50)
    entry_url.pack(side="left", padx=5)
    entry_url.insert(0, "https://books.toscrape.com/")

    ttk.Button(frame_url, text="Scraper les Livres", command=lancer_scraping).pack(side="left", padx=5)

    frame_recherche = ttk.Frame(root)
    frame_recherche.pack(pady=10)

    entry_recherche = ttk.Entry(frame_recherche, width=40)
    entry_recherche.pack(side="left", padx=5)
    ttk.Button(frame_recherche, text="Rechercher", command=rechercher).pack(side="left")

    canvas = tk.Canvas(root, bg="#e6f7ff")
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable = ttk.Frame(canvas)

    scrollable.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    frame_livres = scrollable
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")