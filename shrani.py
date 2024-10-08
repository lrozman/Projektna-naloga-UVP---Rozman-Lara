import csv

def shrani(podatki):
    with open("anime.csv", "w", encoding="utf-8", newline="") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(
            [
                "id",
                "naslov",
                "število epizod",
                "status",
                "sezona premiere",
                "leto premiere",
                "vir",
                "dolzina epizode v minutah",
                "oznaka",
                "ocena",
                "člani",
                "favoritizacije",
                "demografika",
                "teme",
                "žanri",
                "studii",
                "povezani vnosi",
                "glavni liki",
            ]
        )
        for podatek in podatki:
            if len(podatek) > 3: 
                pisatelj.writerow(
                    [
                        podatek["id"],
                        podatek["naslov"],
                        podatek["število epizod"],
                        podatek["status"],
                        podatek["sezona premiere"],
                        podatek["leto premiere"],
                        podatek["vir"],
                        podatek["dolzina epizode v minutah"],
                        podatek["oznaka"],
                        podatek["ocena"],
                        podatek["člani"],
                        podatek["favoritizacije"],
                        podatek["demografika"],
                        podatek["teme"],
                        podatek["zanri"],
                        podatek["studii"],
                        podatek["povezani vnosi"],
                        podatek["glavni liki"],
                    ]
                )
    


    with open("anime_liki.csv", "w", newline="") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["id_lika", "id_anime", "vloga"])
        for podatek in podatki:
            if len(podatek) > 3:
                for lik in podatek["glavni liki"]:
                    pisatelj.writerow([lik[0], podatek["id"], lik[2]])



def shrani_like(podatki_liki):
    with open("liki.csv", "w", newline="") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["id_lika", "ime", "favoritizacije_lika"])
        for lik in podatki_liki:
            pisatelj.writerow([lik[0], lik[1], lik[2]])



def shrani_vse_anime(vsi_anime):
    with open("vsi_anime.csv", "w", encoding="utf-8", newline="") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(
            [
                "id",
                "naslov",
                "število epizod",
                "sezona premiere",
                "leto premiere",
                "vir",
                "dolzina epizode v minutah",
                "ocena",
                "člani",
                "demografika",
                "teme",
                "žanri",
                "studii",
            ]
        )
        for podatek in vsi_anime:
            pisatelj.writerow(
                [
                    podatek["id"],
                    podatek["naslov"],
                    podatek["stevilo epizod"],
                    podatek["sezona premiere"],
                    podatek["leto premiere"],
                    podatek["vir"],
                    podatek["dolzina epizode v minutah"],
                    podatek["ocena"],
                    podatek["člani"],
                    podatek["demografika"],
                    podatek["teme"],
                    podatek["zanri"],
                    podatek["studii"],
                ]
            )
    
    with open("anime_zanri.csv", "w", newline="") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["id", "zanr"])
        for podatek in vsi_anime:
            if len(podatek) > 3:
                for zanr in podatek["zanri"]:
                    pisatelj.writerow([podatek["id"], zanr])


def shrani_fransize(fransize):
    with open("anime_fransize.csv", "w", newline="") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["id_fransize", "id_anime"])
        for fransiza, mnozica in fransize.items():
            for el in mnozica:
                pisatelj.writerow([fransiza, el])
