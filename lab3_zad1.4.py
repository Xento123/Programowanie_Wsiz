# a) Wczytanie imienia i wyświetlenie powitania
imie = input("Podaj imię: ")
print("a) Witaj", imie)

# b) Wczytanie wieku i wyświetlenie komunikatu o wieku
wiek = input("Podaj wiek: ")
print("b) Twój wiek to:", wiek)

# c) Wczytanie imienia i nazwiska, wyświetlenie inicjałów
nazwisko = input("Podaj nazwisko: ")
print("Twoje inicjały to:",imie[0]+nazwisko[0])

# d) Wczytanie łańcucha i wyświetlenie go pięć razy
lancuch = input("Podaj łańcuch: ")
print("d) Powtórzone pięć razy:", lancuch * 5)

# e) Wczytanie dwóch łańcuchów i połączenie ich w trzecim
lanuch1 = input("Podaj pierwszy łańcuch: ")
lanuch2 = input("Podaj drugi łańcuch: ")
polaczone_lancuchy = lanuch1 + lanuch2
print("e) Połączone łańcuchy:", polaczone_lancuchy)

# f) Wczytanie dwóch łańcuchów i utworzenie trzeciego z pierwszej połowy pierwszego i drugiej połowy drugiego
lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")

polowa1 = lancuch1[:len(lancuch1)//2]
polowa2 = lancuch2[len(lancuch2)//2:]

trzeci_lancuch = polowa1 + polowa2
print("f) Trzeci łańcuch:", trzeci_lancuch)