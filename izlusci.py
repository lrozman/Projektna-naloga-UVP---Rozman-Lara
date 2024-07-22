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
        stevilo_epizod = najdba1["ep"]
        status = najdba2["stat"]
        sezona_premiere = najdba3["sez"]
        leto_premiere = najdba3["leto"]

    print(stevilo_epizod, status, sezona_premiere, leto_premiere)

    #lastnosti_re = re.compile(
    #    r'<span class="dark_text">Episodes:</span>.*?(?P<ep>\d+).*?</div>'
    #    r'<span class="dark_text">Status:</span>.*?(?P<stat>\w+).*?</div>'
    #    r'<span class="dark_text">Premiered:</span>.*?<a href="https://myanimelist.net/anime/season/\d+/\w+">(?P<sez>\w+) (?P<leto>\d\d\d\d)</a>', 
    #    flags=re.DOTALL)
    #l_najdba = lastnosti_re.search(besedilo)
    #if l_najdba is not None:
    #    stevilo_epizod = l_najdba["ep"]
    #    status = l_najdba["stat"]
    #    sezona_premiere = l_najdba["sez"]
    #    leto_premiere = l_najdba["leto"]


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
    