import random

planety = ["Merkur", "Venuše", "Země", "Mars", "Jupiter"]

v2 = random.choice(planety)

index = planety.index(v2)+1

print("Vybral jsem planetu: ", v2 ," na indexu: ", index)