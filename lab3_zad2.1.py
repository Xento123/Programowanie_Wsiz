# Wczytanie wartości n i x od użytkownika
n = int(input("Podaj wartość n: "))
x = int(input("Podaj wartość x: "))

# Utworzenie n-elementowej listy składającej się z x-znakowych ciągów
lista_ciagow = [input(f"Podaj {i + 1}. ciąg znakowy ({x} znaków): ")[:x] for i in range(n)]

# Przekonwertowanie listy na krotkę
krotka_ciagow = tuple(lista_ciagow)

# a) Ilość znaków w liście
ilosc_znakow = sum(len(ciag) for ciag in krotka_ciagow)
print("a) Ilość znaków w liście:", ilosc_znakow)

# b) Ilość liter 'k' w liście
ilosc_liter_k = sum(ciag.count('k') for ciag in krotka_ciagow)
print("b) Ilość liter 'k' w liście:", ilosc_liter_k)

# c) Ilość ciągów znaków 'kt' w liście
ilosc_ciagow_kt = sum(ciag.count('kt') for ciag in krotka_ciagow)
print("c) Ilość ciągów znaków 'kt' w liście:", ilosc_ciagow_kt)

# d) Ilość ciągów znaków dłuższych niż s
s = input("Podaj wartość s: ")
ilosc_ciagow_dluzszych_niz_s = sum(1 for ciag in krotka_ciagow if len(ciag) > len(s))
print("d) Ilość ciągów znaków dłuższych niż", s, "w liście:", ilosc_ciagow_dluzszych_niz_s)