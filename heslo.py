import random
napoje = ["čaj", "kafe", "mléko", "džus", "voda"]
vybrany_napoj = random.choice(napoje)
v8 = vybrany_napoj
index = napoje.index(v8)
print("Vybral jsem nápoj " + v8 + " na indexu " + str(index))
