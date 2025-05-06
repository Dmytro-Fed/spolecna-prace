import random
povolani = ["kuchař", "číšník", "programátor", "veterinář", "učitel", "hasič", "lékař"]
v4 = (random.choice(povolani))
index = povolani.index (v4)
print(f"Vybral jsem si {v4} na indexu {index}")
