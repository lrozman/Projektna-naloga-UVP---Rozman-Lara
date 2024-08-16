# Analiza podatkov z myanimelist.net

Za projektno nalogo pri predmetu Uvod v programiranje sem si izbrala analizo anime-jev glede na podatke s spletne strani *myanimelist.net*.
Te sem dobila tako, da sem najprej s funkcijo iz *pridobi.py* pridobila HTML-kode spletnih strani vseh anime sezon (Winter, Spring, Summer, Fall)
od leta 1974 do 2024. Potem sem s funkcijo iz *poisci_anime.py* s spletne strani vsake sezone pridobila seznam anime-jev, ki so se začeli
predvajati tisto sezono in so oblike TV-serij. V datoteki *pridobi.py* sta še funkciji za pridobitev spletne strani posameznega anime-ja in lika.
Iz HTML-kod spletnih strani anime-jev in likov sem s funkcijami iz datoteke *izlusci.py* pridobila podatke o anime-jih oz. likih.
Te podatke sem nato shranila s funkcijami v *shrani.py*. S tem sem ustvarila naslednje CSV-datoteke:
*anime.csv*, *liki.csv* ter povezovalne *anime_liki.csv*, *anime_zanri.csv*, *anime_fransize.csv*.

Potem ko sem pridobila že veliko spletnih strani, sem za pridobivanje novih strani anime-jev in likov večkrat dobila error 405.
Sum je, da si je po več zagonih programa spletna stran zapomnila moj IP in začela ob requestih preverjati, ali sem človek, česar prej
na tej spletni strani še nisem doživela. Iz tega razloga nisem posebej pridobivala še podatkov o studiih, zato so ostali v seznamih.
Da pa bi lahko kljub vsemu naredila analizo na reprezentativnem vzorcu, sem napisala še nekaj funkcij, ki so mi omogočile, 
da sem večino želenih podatkov o anime-jih izluščila iz že pridobljenih spletnih strani vseh sezon. Tako sem dobila 
tabelo *vsi_anime.csv*, ki šteje 5507 vnosov. S to tabelo sem naredila večino analize, ki je izvedena in predstavljena v datoteki *analiza.ipynb*.

## Navodila za uporabo

Najprej so za delovanje programa potrebni naslednji paketi: *requests*, *os*, *re* in *csv*.
V datoteki *main.py* lahko pred zagonom izberete obseg let, za katere naj program pridobi podatke.
To lahko storite v tej vrstici:
`od, do = 1974, 2024`, a zaradi analize priporočam, da ostane taka, kot je.
Nato samo še poženete *main.py*.

Za analizo v *analiza.ipynb* potrebujete naloženo knjižnico *Pandas*, uporabljam pa tudi *matplotlib.pyplot*.