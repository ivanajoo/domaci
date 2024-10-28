#napraviti dictionary koji ima strukturu
#person1: "name" : "Ivana" , "last_name" : "Jonjic"
#person2: "name" : "Ana" , "last_name" : " Anic"
#person3: "name" : " Petar" , "last_name" : "Petrovic"

group={
    "person1":{
        "name" : "Ivana" ,
        "last_name" : "Jonjic"
},
    "person2":{
        "name" : "Ana" ,
    "last_name" : " Anic"
},
    "person3":{
        "name" : " Petar" ,
        "last_name" : "Petrovic"
}
}

print(group["person1"]["last_name"],group["person2"]["name"])
