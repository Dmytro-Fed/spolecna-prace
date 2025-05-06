počasí = ("slunečno", "déšť", "sníh", "mlha", "bouřka")
import random
v5 = random.choice(počasí)
print ("Vybral jsem počas",v5)

import random

zvuky = ["haf", "mňau", "kikirikí", "béé", "kvák"]

zvuk = random.choice(zvuky)

index = zvuky.index(zvuk)

print("Vybral jsem zvuk \"" + zvuk + "\" na indexu " + str(index))

import random
povolani = ["kuchař", "číšník", "programátor", "veterinář", "učitel", "hasič", "lékař"]
v4 = (random.choice(povolani))
index = povolani.index (v4)
print(f"Vybral jsem si {v4} na indexu {index}")
