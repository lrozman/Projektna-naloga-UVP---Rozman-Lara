import csv

def shrani(podatki):
    with open("anime.csv", "w", encoding="utf-8") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(
            [
                "id",
                "naslov",
                "število epizod",
                "status",
                "sezona premiere",
                "leto premiere",
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
            pisatelj.writerow(
                [
                    podatek["id"],
                    podatek["naslov"],
                    podatek["število epizod"],
                    podatek["status"],
                    podatek["sezona premiere"],
                    podatek["leto premiere"],
                    podatek["dolzina epizode v minutah"],
                    podatek["oznaka"],
                    podatek["ocena"],
                    podatek["člani"],
                    podatek["favoritizacije"],
                    podatek["demografika"],
                    podatek["teme"],
                    podatek["žanri"],
                    podatek["studii"],
                    podatek["povezani vnosi"],
                    podatek["glavni liki"],
                ]
            )
    

    with open("anime_zanri.csv", "w") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["id", "zanr"])
        for podatek in podatki:
            for zanr in podatek["žanri"]:
                pisatelj.writerow([podatek["id"], zanr])
    

    with open("anime_liki.csv", "w") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["id_lika", "id_anime", "vloga"])
        for podatek in podatki:
            for lik in podatki["glavni liki"]:
                pisatelj.writerow([lik[0], podatek["id"], lik[2]])


    # Ali naj izluscim se podatke o likih in jih tudi posebej shranim? In franšize? Ali slednje lahko pogrupiram v ipynb?

# Še odprto vprašanje, kam naj dam podatke o likih in kako naj jih obdelujem.
def shrani_like(podatki_liki):
    with open("liki.csv", "w") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["id_lika", "ime", "favoritizacije_lika"])
        #ids = set()
        for lik in podatki_liki:
            #if lik[0] not in ids:
            pisatelj.writerow([lik[0], lik[1], lik[2]])
            #ids.add(lik[0])