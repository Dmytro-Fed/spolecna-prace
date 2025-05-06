import random

zvuky = ["haf", "mňau", "kikirikí", "béé", "kvák"]

zvuk = random.choice(zvuky)

index = zvuky.index(zvuk)

print("Vybral jsem zvuk \"" + zvuk + "\" na indexu " + str(index)
