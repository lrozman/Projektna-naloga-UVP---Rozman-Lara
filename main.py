import pridobi
import poisci_anime
import izlusci
import shrani

od, do = 1974, 2024
sezone = ["winter", "spring", "summer", "fall"]

#pridobi.pridobi_sezone(od, do)

vsi_anime = []
vsi_iz_sezone = []
for leto in range(od, do+1):
    for sezona in sezone:
        animeji = poisci_anime.poisci(leto, sezona)
        vsi_anime.extend(animeji)

        #podatki = izlusci.izlusci_iz_sezone(leto, sezona)
        #vsi_iz_sezone.extend(podatki)

vsi_podatki = []
vsi_liki = []
ids_likov = set()
ids_related = set()
slovar_related = {}
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

    if len(podatki) > 3:
        for lik in podatki["glavni liki"]:
            id_lika = lik[0]
            if id_lika not in ids_likov:
                ids_likov.add(id_lika)
                pridobi.pridobi_lik(id_lika)
                try:
                    podatki_lik = izlusci.izlusci_lik(id_lika)
                except FileNotFoundError:
                    continue
                if podatki_lik:
                    vsi_liki.append(podatki_lik)
    
    # Katera podatkovna struktura bi bila najbolj primerna za to?
        mnozica_id = set()
        for rel_id, related in podatki["povezani vnosi"]:
            mnozica_id.add(rel_id)
        mnozica_id.add(id)

        for rel_id, related in podatki["povezani vnosi"]:
            if rel_id in slovar_related:
                slovar_related[rel_id].union(mnozica_id)  # Torej je ključ tudi v vrednostih
                ids_related.union(mnozica_id)
                break  # Predvidevam, da so povezani vnosi urejeni bodisi obojestransko bodisi imajo novejše serije za povezane vnose vse svoje predhodnike.
        
        if id not in ids_related: # Če je id že bil related, dvomim, da se torej ne bi našel povezan vnos, ki je ključ v slovarju. Ker še ni bil, prej funkcija ni našla ključa.
            slovar_related[id] = mnozica_id
        # Upamo na najboljše.
        
          

shrani.shrani(vsi_podatki)
shrani.shrani_like(vsi_liki)
#shrani.shrani_vse_anime(vsi_iz_sezone)
shrani.shrani_fransize(slovar_related)