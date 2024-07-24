import pridobi
import poisci_anime
import izlusci
import shrani

#od, do = 1974, 2024
od, do = 1974, 2024
sezone = ["winter", "spring", "summer", "fall"]

#pridobi.pridobi_sezone(od, do)

vsi_anime = []
for leto in range(od, do):
    for sezona in sezone:
        animeji = poisci_anime.poisci(leto, sezona)
        vsi_anime.extend(animeji)

vsi_podatki = []
vsi_liki = []
ids_likov = set()
for anime in vsi_anime:
    id = anime[1]
    naslov = anime[0]
    pridobi.pridobi_anime(id, naslov)
    try:
        podatki = izlusci.izlusci_anime(id)
    except FileNotFoundError:
        continue
    podatki["naslov"] = naslov
    podatki["id"] = id
    vsi_podatki.append(podatki)

    #for lik in podatki["glavni liki"]:
    #    id_lika = lik[0]
    #    if id_lika not in ids_likov:
    #        if pridobi.pridobi_lik(id_lika) is not None:
    #            podatki_lik = izlusci.izlusci_lik(id_lika)
    #            vsi_liki.append(podatki_lik)
    #        ids_likov.add(id_lika)

shrani.shrani(vsi_podatki)
shrani.shrani(vsi_liki)