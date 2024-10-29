from pprint import pprint

pin_code= 3124

#ako je tajni pin 4231 ILI ako je tajni pin 3124 ispisati poruku " pin je tocan"
#u suprotnom ispisati "pin je noteocan"
#koristiti samo 1 if + 1 else

if pin_code == 4231 or pin_code == 3124:
    print("Pin je tocan")
else:
    print("Pin je netocan")