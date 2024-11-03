
#svaka prodavnica ima svoje ime,svaka prodavnica ima svjoe proizvode i cijene

shops = {
    "Maxi":{
        "kruh":100,
        "novine":50
    },

     "Idea:":{
         "kruh":140,
         "novine":40
    },
    "Road:":{
         "kruh":120,
         "novine":40
    },
    "Freeshop:":{

         "novine":40
    }
}
total_bread_price=0
total_bread_shops=0
highest_price=0
highest_bread_price_shop=0

for shop_name,items in shops.items():
    if "kruh" in items:
        total_bread_price += items["kruh"]
        total_bread_shops+=1

        if items["kruh"] > highest_price:
            highest_price = items["kruh"]
            highest_bread_price_shop = shop_name


average_bread_price=total_bread_price/total_bread_shops

print("Prosjecna cijena kruha je : " ,average_bread_price)
print("Najvisa cijena kruha " ,highest_price)
print("Prodavnica koja ima najvisu cijenu kruha je : ", highest_bread_price_shop)

