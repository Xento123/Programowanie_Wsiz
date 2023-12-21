wysokosc = int(input("Podaj wysokość choinki: "))

for i in range(1, wysokosc + 1):
    spacje = wysokosc - i
    gwiazdki = 2 * i - 1
    print(" " * spacje + "*" * gwiazdki)

trzon_szerokosc = wysokosc // 3
trzon_wysokosc = wysokosc // 3

for _ in range(trzon_wysokosc):
    spacje_trzon = wysokosc - trzon_szerokosc // 2
    print(" " * spacje_trzon + "|" * trzon_szerokosc)