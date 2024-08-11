import requests
import os

def pridobi_sezone(od, do):
    sezone = ["winter", "spring", "summer", "fall"]

    headers = {"User-agent": "Chrome/124.0.6367.202"}
    
    for leto in range(od, do+1):
        for sezona in sezone:
            url = f"https://myanimelist.net/anime/season/{leto}/{sezona}"

            odgovor = requests.get(url, headers=headers)
            if odgovor.status_code != 200:
                print("Napaka", leto, sezona, odgovor.status_code)
                return
            
            with open(os.path.join("Neobdelani_podatki", "Sezone", f"anime{leto}{sezona}.html"), "w", encoding="utf-8") as dat:
                dat.write(odgovor.text)



def pridobi_anime(id, naslov):

    headers = {"User-agent": "Chrome/124.0.6367.202"}

    naslov = naslov.replace(" ", "_")
    
    url = f"https://myanimelist.net/anime/{id}/{naslov}"

    odgovor = requests.get(url, headers=headers)
    if odgovor.status_code != 200:
        print("Napaka", id, odgovor.status_code)
        return
    
    with open(os.path.join("Neobdelani_podatki", "anime", f"anime{id}.html"), "w", encoding="utf-8") as dat:
        dat.write(odgovor.text)



def pridobi_lik(id_lika):

    headers = {"User-agent": "Chrome/124.0.6367.202"}

    url = f"https://myanimelist.net/character/{id_lika}"

    odgovor = requests.get(url, headers=headers)
    if odgovor.status_code != 200:
        print("Napaka: lik", id_lika, odgovor.status_code)
        return
    
    with open(os.path.join("Neobdelani_podatki", "Liki", f"lik{id_lika}.html"), "w", encoding="utf-8") as dat:
        dat.write(odgovor.text)
    
    