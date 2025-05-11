
import random
osobnosti = ["Einstein", "Newton", "Tesla", "Curie", "Hawking"]
vybrana_osobnost = random.choice(osobnosti)
v1 = vybrana_osobnost
index = osobnosti.index(v1)
print("Vybral jsem osobnost" + v1 + "na indexu" + str(index))


import random
kreatury = ["drak", "elf", "obr", "skřítek", "čaroděj"]
v6 = random.choice(kreatury)
index = kreatury.index (v6)
print (f"Vybral jsem tvora {v6} na indexu {index}")

import random
počasí = ("slunečno", "déšť", "sníh", "mlha", "bouřka")
v5 = random.choice(počasí)
index = počasí.index (v5)
print ("Vybral jsem počas",v5)

import random
zvuky = ["haf", "mňau", "kikirikí", "béé", "kvák"]
v3 = random.choice(zvuky)
index = zvuky.index(v3)
print("Vybral jsem zvuk \"" + zvuk + "\" na indexu " + str(index))

import random
povolani = ["kuchař", "číšník", "programátor", "veterinář", "učitel", "hasič", "lékař"]
v4 = (random.choice(povolani))
index = povolani.index (v4)
print(f"Vybral jsem si {v4} na indexu {index}")

