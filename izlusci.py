import re
import os

def izlusci_anime(id):

    with open(os.path.join("Neobdelani_podatki", "anime", f"anime{id}.html"), "r", encoding="utf-8") as dat:
        besedilo = dat.read()


    # Izluscimo podatke o številu epizod, statusu in sezoni premiere
    st_epizod_re = r'<span class="dark_text">Episodes:</span>.*?(?P<ep>\d+).*?</div>'
    najdba1 = re.search(st_epizod_re, besedilo, flags=re.DOTALL)

    status_re = r'<span class="dark_text">Status:</span>.*?(?P<stat>\w+ \w+).*?</div>'
    najdba2 = re.search(status_re, besedilo, flags=re.DOTALL)

    sezona_re = r'<span class="dark_text">Premiered:</span>.*?<a href="https://myanimelist.net/anime/season/\d+/\w+">(?P<sez>\w+) (?P<leto>\d\d\d\d)</a>'
    najdba3 = re.search(sezona_re, besedilo, flags=re.DOTALL)

    if najdba1 is None or najdba2 is None or najdba3 is None:
        print("Napaka: lastnosti", id)
    
    else:
        stevilo_epizod = int(najdba1["ep"])
        status = najdba2["stat"]
        sezona_premiere = najdba3["sez"]
        leto_premiere = int(najdba3["leto"])

    print(stevilo_epizod, status, sezona_premiere, leto_premiere)

    # Izluscimo vrsto vira:
    vir_re1 = r'<span class="dark_text">Source:</span>(.*?)</div>'
    najdba1 = re.search(vir_re1, besedilo, flags=re.DOTALL)
    if najdba1 is not None:
        s = najdba1.group(1).strip().split("\n")
        if len(s) == 1:
            vir = najdba1.group(1).strip()
        else:
            vir_re2 = r'<a href="https://myanimelist.net/anime/\d+/\S+>.*?(\w+ ?\w+?).*?</a>'
            najdba2 = re.search(vir_re2, najdba1.group(1), flags=re.DOTALL)
            if najdba2 is not None:
                vir = najdba2.group(1)
    else:
        print("Napaka: vir", id)

    print(vir)

    # Izluscimo dolzino epizode in rating
    dolzina_re = re.compile(r'<span class="dark_text">Duration:</span>\s+(\d+) min. per ep')
    najdba = dolzina_re.search(besedilo)
    if najdba is not None:
        dolzina_ep_minute = int(najdba.group(1))
    else:
        print("Napaka: dolzina", id)

    rating_re = re.compile(r'<span class="dark_text">Rating:</span>\s+(.*?)\s+</div>')
    najdba = rating_re.search(besedilo)
    if najdba is not None:
        rating = najdba.group(1)                                    #V kakšnem formatu želim rating?
    else:
        print("Napak: rating", id)
    
    print(dolzina_ep_minute, rating)
    

    # Izluscimo oceno, stevilo uporabnikov (members) in stevilo favorizacij
    ocena_re = re.compile(r'<span itemprop="ratingValue" class="score-label score-\d">(\d.\d\d)</span>')
    najdba = ocena_re.search(besedilo)
    if najdba is not None:
        ocena = float(najdba.group(1))
    else:
        print("Napaka: ocena", id)
    
    members_re = re.compile(r'<span class="dark_text">Members:</span>\s+(\d+,?\d+,?\d+)')
    najdba = members_re.search(besedilo)
    if najdba is not None:
        members = int(najdba.group(1).replace(",", ""))
    else:
        print("Napaka: members", id)
    
    fave_re = re.compile(r'<span class="dark_text">Favorites:</span>\s+(\d+,?\d+)')
    najdba = fave_re.search(besedilo)
    if najdba is not None:
        favoritizacije = int(najdba.group(1).replace(",", ""))
    else:
        print("Napaka: favoritizacije", id)
    
    print(ocena, members, favoritizacije)

    # Izluscimo demografiko
    if besedilo.find('<span class="dark_text">Demographic:</span>') == -1:
        demografika = "NG"
    else:
        demogr_re = re.compile(
            r'<span class="dark_text">Demographic:</span>\s+'
            r'<span itemprop="genre" style="display: none">'
            r'(\w+)</span>'
        )
        najdba = demogr_re.search(besedilo)
        if najdba is not None:
            demografika = najdba.group(1)
        else:
            print("Napaka: demografika", id)
    
    print(demografika)
    
    # Izluscimo teme
    teme = []
    teme_re1 = re.compile(r'<span class="dark_text">Themes?:</span>(.*?)</div>', flags=re.DOTALL)
    najdba1 = teme_re1.search(besedilo)
    if najdba1 is not None:
        teme_re2 = re.compile(r'<span itemprop="genre" style="display: none">(.*?)</span>')
        for najdba in teme_re2.finditer(najdba1.group(1)):
            tema = najdba.group(1)
            teme.append(tema)
    else:
        print("Napaka: teme", id)
    
    print(teme)




    