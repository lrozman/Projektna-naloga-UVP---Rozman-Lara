import re
import os

def izlusci_anime(id):
    """Funkcija izlušči podatke o anime-ju iz pridobljene HTML-strani in vrne slovar lastnosti."""

    with open(os.path.join("Neobdelani_podatki", "anime", f"anime{id}.html"), "r", encoding="utf-8") as dat:
        besedilo = dat.read()


    # Izluscimo podatke o številu epizod, statusu in sezoni premiere.
    st_epizod_re = r'<span class="dark_text">Episodes:</span>.*?(?P<ep>\d+).*?</div>'
    najdba1 = re.search(st_epizod_re, besedilo, flags=re.DOTALL)

    status_re = r'<span class="dark_text">Status:</span>.*?(?P<stat>\w+ \w+).*?</div>'
    najdba2 = re.search(status_re, besedilo, flags=re.DOTALL)

    sezona_re = r'<span class="dark_text">Premiered:</span>.*?<a href="https://myanimelist.net/anime/season/\d+/\w+">(?P<sez>\w+) (?P<leto>\d\d\d\d)</a>'
    najdba3 = re.search(sezona_re, besedilo, flags=re.DOTALL)

    if najdba1 is None or najdba2 is None or najdba3 is None:
        print("Napaka: lastnosti", id)
        return {}
    
    else:
        stevilo_epizod = int(najdba1["ep"])
        status = najdba2["stat"]
        sezona_premiere = najdba3["sez"]
        leto_premiere = int(najdba3["leto"])


    # Izluscimo vrsto vira.
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


    # Izluscimo povprecno dolzino epizode in oznako.
    dolzina_re = re.compile(r'<span class="dark_text">Duration:</span>\s+(\d+) min')
    najdba = dolzina_re.search(besedilo)
    if najdba is not None:
        dolzina_ep_minute = int(najdba.group(1))
    else:
        print("Napaka: dolzina", id)
        dolzina_ep_minute = "Unknown"

    oznaka_re = re.compile(r'<span class="dark_text">Rating:</span>\s+(.*?)\s+</div>')
    najdba = oznaka_re.search(besedilo)
    if najdba is not None:
        oznaka = najdba.group(1)                                                             # V kakšnem formatu želim rating?
    else:
        print("Napak: oznaka", id)
    

    # Izluscimo oceno, stevilo uporabnikov (members) in stevilo favorizacij.
    ocena_re = re.compile(r'<span itemprop="ratingValue" class="score-label score-\d">(\d.\d\d)</span>')
    najdba = ocena_re.search(besedilo)
    if najdba is not None:
        ocena = float(najdba.group(1))
    else:
        print("Napaka: ocena", id)
        ocena = "N/A"
    
    members_re = re.compile(r'<span class="dark_text">Members:</span>\s+(\d+,?\d*,?\d*)')
    najdba = members_re.search(besedilo)
    if najdba is not None:
        members = int(najdba.group(1).replace(",", ""))
    else:
        print("Napaka: members", id)
    
    fave_re = re.compile(r'<span class="dark_text">Favorites:</span>\s+(\d+,?\d*)')
    najdba = fave_re.search(besedilo)
    if najdba is not None:
        favoritizacije = int(najdba.group(1).replace(",", ""))
    else:
        print("Napaka: favoritizacije", id)
    

    # Izluscimo demografiko.
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
    
    
    # Izluscimo teme.
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
    

    # Izluscimo zanre.
    zanri = []
    zanri_re1 = re.compile(r'<span class="dark_text">Genres?:</span>(.*?)</div>', flags=re.DOTALL)
    najdba1 = zanri_re1.search(besedilo)
    if najdba1 is not None:
        zanri_re2 = re.compile(r'<span itemprop="genre" style="display: none">(.*?)</span>')
        for najdba in zanri_re2.finditer(najdba1.group(1)):
            zanr = najdba.group(1)
            zanri.append(zanr)
    else:
        print("Napaka: zanri", id)
    

    # Izluscimo animacijski studio.
    studii = []
    studii_re1 = re.compile(r'<span class="dark_text">Studios:</span>(.*?)</div>', flags=re.DOTALL)
    najdba1 = studii_re1.search(besedilo)
    if najdba1 is not None:
        studii_re2 = re.compile(r'<a href="/anime/producer/(?P<id>\d+)/\S*?" title=".*?">(?P<ime>.*?)</a>')
        for najdba in studii_re2.finditer(najdba1.group(1)):
            studii.append((najdba["id"], najdba["ime"]))                               # Ali id-jem studia dodam predpono "s"?
    else:
        print("Napaka: studii", id)
    

    # Izluscimo povezane vnose (related entries) - to so nadaljevanja, predzgodbe in druge povezane vsebine, obravnavane na myanimelist.net.
    # Ker se ukvarjam samo z anime-ji v obliki serij, bom izluscila samo take povezane vnose.
    povezani_vnosi = []
    povezani_re1 = re.compile(
        r'<h2 id="related_entries">Related Entries</h2></div></div><div class="related-entries">(.*?)<div class="widget-content">', 
        flags=re.DOTALL)
    najdba1 = povezani_re1.search(besedilo)
    if najdba1 is not None:
        povezani_re2 = re.compile(r'<div class="content">(.*?)</a>', flags=re.DOTALL)
        for najdba in povezani_re2.finditer(najdba1.group(1)):
            if najdba.group().find("TV") != -1:
                najdba3 = re.search(r'<a href="https://myanimelist.net/anime/(?P<id>\d+)/\S*?>\s+(?P<naslov>.*?)\s+</a>', najdba.group())
                povezani_vnosi.append((najdba3["id"], najdba3["naslov"].strip()))
    else:
        print("Napaka: povezani vnosi", id)
    

    # Izluscimo 10 najpomembnejsih likov, ki so navedeni na začetni strani posameznega anime-ja,
    # tako da za vsakega ustvarimo nabor lastnosti: id lika, ime lika, vloga lika ("Supporting" oz. "Main").
    liki = []
    liki_re = re.compile(
        r'<h3 class="h3_characters_voice_actors"><a href="https://myanimelist.net/character/(?P<id>\d+)/\S+">(?P<ime>.*?)</a></h3>'
        r'\s+?<div class="spaceit_pad">\s+<small>(?P<vloga>\w+)</small>'
        )
    for najdba in liki_re.finditer(besedilo):
        liki.append((najdba["id"], najdba["ime"], najdba["vloga"]))                         # Ali dodam še Supporting/Main?
    

    return {
        "število epizod": stevilo_epizod,
        "status": status,
        "sezona premiere": sezona_premiere,
        "leto premiere": leto_premiere,
        "vir": vir,
        "dolzina epizode v minutah": dolzina_ep_minute,
        "oznaka": oznaka,
        "ocena": ocena,
        "člani": members,
        "favoritizacije": favoritizacije,
        "demografika": demografika,                           # Ciljna skupina?
        "teme": teme,
        "žanri": zanri,
        "studii": studii,
        "povezani vnosi": povezani_vnosi,
        "glavni liki": liki
    }





# Še odprto vprašanje, kam gre ta del in kako se bom lotila likov; ali lahko to dodam izluscevanju podatkov o liku zgoraj
# ali mi bo to laže za analizo.
def izlusci_lik(id_lika):
    """Funkcija iz pridobljene HTML-strani vsakega lika izlušči podatke o njem in vrne nabor lastnosti."""

    with open(os.path.join("Neobdelani_podatki", "Liki", f"lik{id_lika}.html"), "r", encoding="utf-8") as dat:
        besedilo_l = dat.read()

    faves_re = re.compile(r'Member Favorites: (\d+,?\d*)\b')
    najdba = faves_re.search(besedilo_l)
    if najdba is not None:
        lik_faves = int(najdba.group(1).replace(",", ""))
    else:
        print("Napaka: lik_faves", id_lika)
    
    ime_re = re.compile(r'<title>\s+(.*)\(.*?\s+</title>')
    najdba = ime_re.search(besedilo_l)
    if najdba is not None:
        lik_ime = najdba.group(1).rstrip()
    else:
        print("Napaka: ime lika", id_lika)
    
    return id_lika, lik_ime, lik_faves
