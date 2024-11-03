from itertools import product

#pitajte korinika da unese ime proizvoda
#kaada unese ime proizvoda dodati proizvod u "kasu"
#korisnik mora unijeti 3 proizvoda ukupno

kasa = []

while len(kasa) < 3:
    item=input("Unesite ime proizvoda: ")
    kasa.append(item)
    print(kasa)