Main 

# main.py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import io
from interface import creer_interface_principale

def animer_texte(texte, label, index=0):
    if index < len(texte):
        label.config(text=texte[:index+1])
        label.after(50, lambda: animer_texte(texte, label, index+1))

def charger_fond(root):
    url_img = "https://tse2.mm.bing.net/th/id/OIP.JkyOpToNKftP15k5dxJvIAHaHa?rs=1&pid=ImgDetMain"
    data = requests.get(url_img).content
    image = Image.open(io.BytesIO(data)).resize((700, 800))
    background = ImageTk.PhotoImage(image)

    fond = tk.Label(root, image=background)
    fond.image = background
    fond.place(x=0, y=0, relwidth=1, relheight=1)

def main():
    root = tk.Tk()
    root.title("Bibliothèque de Livres")
    root.geometry("700x800")

    charger_fond(root)

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12))
    style.configure("TLabel", font=("Helvetica", 11))
    style.configure("Texte.TLabel", font=("Helvetica", 11), background="#ffffff")
    style.configure("Livre.TFrame", background="#ffffff", relief="raised", borderwidth=2)

    frame_bienvenue = ttk.Frame(root)
    frame_bienvenue.pack(expand=True)

    label_bienvenue = ttk.Label(frame_bienvenue, text="", font=("Helvetica", 20, "bold"), background="#e6f7ff")
    label_bienvenue.pack(pady=20)

    animer_texte("Bienvenue dans la Bibliothèque de Livres 📚 !", label_bienvenue)

    sous_label = ttk.Label(
        frame_bienvenue,
        text="Clique sur 'Commencer' pour explorer les livres !",
        font=("Helvetica", 14),
        background="#e6f7ff"
    )
    sous_label.pack(pady=10)

    def commencer():
        frame_bienvenue.destroy()
        creer_interface_principale(root)

    ttk.Button(frame_bienvenue, text="Commencer", command=commencer).pack(pady=20)

    root.mainloop()

if _name_ == "_main_":
    main()