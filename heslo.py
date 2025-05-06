import random
osobnosti = ["Einstein", "Newton", "Tesla", "Curie", "Hawking"]
vybrana_osobnost = random.choice(osobnosti)
v1 = vybrana_osobnost
index = osobnosti.index(v1)
print("Vybral jsem osobnost" + v1 + "na indexu" + str(index))
