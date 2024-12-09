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

allowed_options=["dodaj","obrisi","izlistaj","stop","history","obrisi sve","najskuplji"]
option=None
history=[]
while option not in allowed_options:
    option = input(f"Sta zelite da radite ? {",".join(allowed_options)} \n").lower()

    if option == "obrisi":
        product=None

        while product not in products:
            product = input("Unesite ime proizvoda za brisanje:\n ").lower()

        del products[product]
        msg=f"Obristali ste proizvod: {product} \n"
        print(msg)
        history.append(msg)
        option=None

    elif option == "dodaj":

        product=None

        while product in products or product is None:
            product=input("Unesite ime proizvoda koje ne postoji: \n").lower()

        product_price = None
        while product_price is None or product_price <=0:
            product_price = int(input("Unesite cijenu proizvoda: \n "))

        product_amount = None
        while product_amount is None or product_amount <= 0:
            product_amount = int(input("Unesite kolicinu proizvoda: \n"))

        products[product] = {
            "cena":product_price,
            "kolicina":product_amount
        }
        option=None
        msg=f"Dodali ste novi proizvod: {product} \n"
        print(msg)
        history.append(msg)

    elif option == "izlistaj":
        print(products)
        option=None
    elif option == "history":
        print(history)
        option=None
    elif option == "obrisi sve":
        products={}
        option=None
    elif option == "najskuplji":
        najvisa_cijena = 0
        najskuplji_product = None
        for product in products:
            if najvisa_cijena < products[product]["cena"]:
                najvisa_cijena = products[product]["cena"]
                najskuplji_product=product
        print(f"Najskuplji proizvod je:  {najskuplji_product}", f" i cijena mu je: {najvisa_cijena}")


print(products)
