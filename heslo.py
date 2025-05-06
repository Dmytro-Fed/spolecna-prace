import random

# Definice barev a hodnot karet
COLORS = ['Červená', 'Modrá', 'Zelená', 'Žlutá']
VALUES = [str(i) for i in range(1, 10)] + ['Přeskoč', 'Změna směru', 'Tahy navíc']

# Funkce pro vytvoření balíčku karet
def vytvor_balicek():
    balicek = []
    for color in COLORS:
        for value in VALUES:
            balicek.append(f"{color} {value}")
    random.shuffle(balicek)
    return balicek

# Inicializace hry
def inicializace_hry():
    balicek = vytvor_balicek()
    hrac_1_ruka = [balicek.pop() for _ in range(7)]
    hrac_2_ruka = [balicek.pop() for _ in range(7)]
    odkladaci_balicek = [balicek.pop()]
    return balicek, odkladaci_balicek, hrac_1_ruka, hrac_2_ruka

# Funkce pro kontrolu, zda je tah platný
def je_tah_platny(hrana_karta, vybrana_karta):
    barva_shoda = hrana_karta.split()[0] == vybrana_karta.split()[0]
    hodnota_shoda = hrana_karta.split()[1] == vybrana_karta.split()[1]
    return barva_shoda or hodnota_shoda

# Hlavní logika hry
def hraj_uno():
    balicek, odkladaci_balicek, hrac_1_ruka, hrac_2_ruka = inicializace_hry()
    tah_hrace = 1

    while True:
        print(f"\nKarta nahoře: {odkladaci_balicek[-1]}")
        if tah_hrace == 1:
            print(f"Hráč 1: {hrac_1_ruka}")
            aktualni_hrac = hrac_1_ruka
        else:
            print(f"Hráč 2: {hrac_2_ruka}")
            aktualni_hrac = hrac_2_ruka

        vyber_karty = input("Vyberte kartu (zadejte číslo pozice karty) nebo napište 'tahat' pro tahání karty: ")

        if vyber_karty.lower() == 'tahat':
            if balicek:
                nova_karta = balicek.pop()
                print(f"Táhli jste kartu: {nova_karta}")
                aktualni_hrac.append(nova_karta)
            else:
                print("Balíček je prázdný! Hra končí remízou.")
                break
        else:
            try:
                vybrana_karta = aktualni_hrac[int(vyber_karty) - 1]
                if je_tah_platny(odkladaci_balicek[-1], vybrana_karta):
                    odkladaci_balicek.append(vybrana_karta)
                    aktualni_hrac.remove(vybrana_karta)
                    if not aktualni_hrac:
                        print(f"Hráč {tah_hrace} vyhrál!")
                        break
                else:
                    print("Neplatný tah, zkuste to znovu.")
            except (ValueError, IndexError):
                print("Neplatná volba, zkuste to znovu.")

        tah_hrace = 3 - tah_hrace  # Přepnutí mezi hráčem 1 a 2

# Spuštění hry
hraj_uno()
