import requests
import os

def pridobi_sezone(od, do):
    sezone = ["winter", "spring", "summer", "fall"]

    headers = {"User-agent": "Chrome/124.0.6367.202"}
    
    for leto in range(od, do):
        for sezona in sezone:
            url = f"https://myanimelist.net/anime/season/{leto}/{sezona}"

            odgovor = requests.get(url, headers=headers)
            if odgovor.status_code != 200:
                print("Napaka", leto, sezona, odgovor.status_code)
                return
            
            with open(os.path.join("Neobdelani_podatki", "Sezone", f"anime{leto}{sezona}.html"), "w", encoding="utf-8") as dat:
                dat.write(odgovor.text)
            