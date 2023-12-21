def oblicz_silnie(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * oblicz_silnie(n - 1)

n = int(input("Podaj liczbę naturalną n: "))

if n < 0:
    print("Liczba naturalna musi być nieujemna.")
else:
    wynik = oblicz_silnie(n)
    print(f"{n}! = {wynik}")