imiona = ["Kacper", "Adrian", "Zuzia", "Elwira"]

# a) Sortowanie alfabetyczne i wyświetlanie
imiona.sort()
print("a) Posortowane imiona:", imiona)

# b) Dodawanie dwóch osób na końcu i pobieranie ostatniej z nich
imiona.extend(["Kinga", "Mateusz"])
ostatnia_osoba = imiona.pop()
print("b) Lista po dodaniu i pobraniu:", imiona)
print("   Ostatnia osoba:", ostatnia_osoba)

# c) Dodawanie jeszcze jednej osoby na pozycji 3
imiona.insert(2, "Ewa")
print("c) Lista po dodaniu na pozycji 3:", imiona)

# d) Odwracanie kolejności listy i zdublowanie
imiona.reverse()
imiona_dubel = imiona * 2
print("d) Odwrócona i zdublowana lista:", imiona_dubel)