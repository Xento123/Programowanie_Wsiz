while True:
    try:
        liczba = int(input("Podaj liczbę całkowitą: "))
        if liczba < 0:
            print("Podano liczbę ujemną. Koniec programu.")
            break
        else:
            print(f"Podano liczbę dodatnią: {liczba}")
    except ValueError:
        print("Nieprawidłowy format. Podaj liczbę całkowitą.")