Scraping 

# scraping.py
import requests
from bs4 import BeautifulSoup

def scraper_livres(url):
    """Scrape les livres depuis l'URL donnée."""
    livres_data = []

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        for article in soup.find_all("article", class_="product_pod"):
            titre = article.h3.a["title"]
            prix = article.find("p", class_="price_color").text
            img_src = article.find("img")["src"]

            if img_src.startswith("../"):
                img_src = url + img_src.replace("../", "")
            elif img_src.startswith("./"):
                img_src = url + img_src.replace("./", "")
            else:
                img_src = url + img_src

            livres_data.append((titre, prix, img_src))

    except Exception as e:
        print("Erreur lors du scraping :", e)

    return livres_data