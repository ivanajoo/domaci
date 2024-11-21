

products = {
    "helb": {
        "cena": 100,
        "kolicina" : 50
    },
    "pivo" :{
        "cena":50,
        "kolicina":220
    }
}

print(products)

option=None

while option not in ["dodaj","obrisi"]:
    option = input("Sta zelite da radite [dodaj] ili [obrisi]: ").lower()

    if option == "obrisi":
        product=None

        while product not in products:
            product = input("unseite ime proizvoda za brisanje: ").lower()

        del products[product]
        print(products)

    elif option == "dodaj":

        product=None

        while product in products or product is None:
            product=input("unseite ime proizvoda koje ne postoji ").lower()
        try:
            cena = float(input(f"Unesite cenu za proizvod '{product}': "))
            kolicina = int(input(f"Unesite količinu za proizvod '{product}': "))
            products[product] = {"cena": cena, "kolicina": kolicina}
            print("Proizvod je uspješno dodan.")
        except ValueError:
            print("Greška u unosu. Pokušajte ponovo.")

        print(products)