# affichage.py
import requests
import io
from PIL import Image, ImageTk
from tkinter import ttk

def afficher_livres(frame_livres, livres):
    """Affiche les livres dans la zone prévue."""
    for widget in frame_livres.winfo_children():
        widget.destroy()

    for titre, prix, img_url in livres:
        try:
            img_data = requests.get(img_url).content
            img = Image.open(io.BytesIO(img_data)).resize((80, 100))
            photo = ImageTk.PhotoImage(img)

            bloc = ttk.Frame(frame_livres, style="Livre.TFrame")
            bloc.pack(pady=10, padx=10, fill="x")

            label_img = ttk.Label(bloc, image=photo)
            label_img.image = photo
            label_img.pack(side="left")

            texte = f"{titre}\n{prix}"
            label_texte = ttk.Label(bloc, text=texte, style="Texte.TLabel")
            label_texte.pack(side="left", padx=10)

        except Exception:
            continue