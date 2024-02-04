tekst = "Python jest super"

# a) Zerowy i ostatni znak
zerowy_znak = tekst[0]
ostatni_znak = tekst[-1]

print("a) Zerowy znak:", zerowy_znak)
print("   Ostatni znak:", ostatni_znak)

# b) Co drugi znak, zaczynając od zerowego
co_drugi_znak = tekst[::2]

print("b) Co drugi znak, zaczynając od zerowego:", co_drugi_znak)

# c) Co trzeci znak, zaczynając od pierwszego
co_trzeci_znak = tekst[1::3]

print("c) Co trzeci znak, zaczynając od pierwszego:", co_trzeci_znak)

# d) Od dziesiątego do ostatniego znaku
od_dziesiatego_do_ostatniego = tekst[9:]

print("d) Od dziesiątego do ostatniego znaku:", od_dziesiatego_do_ostatniego)

# e) Od końca do początku
od_konca_do_poczatku = tekst[::-1]

print("e) Od końca do początku:", od_konca_do_poczatku)