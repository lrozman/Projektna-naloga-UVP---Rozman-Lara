import os
import re

def poisci(leto, sezona):
    """Funkcija v HTML datoteki sezone poišče naslov in id posamezne anime serije, ki se je začela to sezono. Vrne seznam parov."""

    with open(os.path.join("Neobdelani_podatki", "Sezone", f"anime{leto}{sezona}.html"), "r", encoding="utf-8") as dat:
        vsebina = dat.read()        

        # Celoten HTML vključuje tudi filme, ONA, OVA in posebne epizode, ki so prav tako vrednotene na myanimelist.net.
        # Nas zanimajo le novo prihajajoče anime serije, ki se vedno nahajajo v prvem razdelku strani posamezne sezone. 
        vzorec_za_iskano = r'<div class="anime-header">TV \(New\)</div>(.*)<div class="anime-header">TV \(Continuing\)</div>'
        iskana_vsebina = (re.search(vzorec_za_iskano, vsebina, flags=re.DOTALL)).group(1)

        vzorec_anime = r'<h2 class="h2_anime_title"><a href="https://myanimelist.net/anime/(?P<id>\d+).+class="link-title">(?P<naslov>.+)</a></h2></div>'
        anime = []
        for najdba in re.finditer(vzorec_anime, iskana_vsebina):
            anime.append((najdba["naslov"], najdba["id"]))      

    return anime  
