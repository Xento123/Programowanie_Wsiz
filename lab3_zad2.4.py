import random

a = random.randint(3, 7)
b = random.randint(3, 7)

X = {random.randint(0, 10) for _ in range(a)}
Y = {random.randint(0, 10) for _ in range(b)}

# a) Czy zbiór X zawiera liczbę 5
czy_zawiera_5_X = 5 in X
print("a) Zbiór X zawiera liczbę 5:", czy_zawiera_5_X)

# b) Czy zbiór X jest podzbiorem zbioru Y
czy_podzbior_X_Y = X.issubset(Y)
print("b) Zbiór X jest podzbiorem zbioru Y:", czy_podzbior_X_Y)

# c) Czy zbiór Y jest podzbiorem zbioru X
czy_podzbior_Y_X = Y.issubset(X)
print("c) Zbiór Y jest podzbiorem zbioru X:", czy_podzbior_Y_X)

# d) Czy zbiór X jest nadzbiorem zbioru Y
czy_nadzbior_X_Y = X.issuperset(Y)
print("d) Zbiór X jest nadzbiorem zbioru Y:", czy_nadzbior_X_Y)

# e) Czy zbiór Y jest nadzbiorem zbioru X
czy_nadzbior_Y_X = Y.issuperset(X)
print("e) Zbiór Y jest nadzbiorem zbioru X:", czy_nadzbior_Y_X)

# f) Suma zbiorów X i Y
suma_zbiorow = X.union(Y)
print("f) Suma zbiorów X i Y:", suma_zbiorow)

# g) Różnica zbiorów X i Y
roznica_X_Y = X.difference(Y)
print("g) Różnica zbiorów X i Y:", roznica_X_Y)

# h) Różnica zbiorów Y i X
roznica_Y_X = Y.difference(X)
print("h) Różnica zbiorów Y i X:", roznica_Y_X)

# i) Iloczyn zbiorów X i Y
iloczyn_zbiorow = X.intersection(Y)
print("i) Iloczyn zbiorów X i Y:", iloczyn_zbiorow)

# j) Różnica symetryczna zbiorów X i Y
roznica_symetryczna_X_Y = X.symmetric_difference(Y)
print("j) Różnica symetryczna zbiorów X i Y:", roznica_symetryczna_X_Y)

# k) Wartość najwyższego elementu w obu zbiorach
najwyzszy_element_X = max(X)
najwyzszy_element_Y = max(Y)
print("k) Najwyższy element w zbiorze X:", najwyzszy_element_X)
print("   Najwyższy element w zbiorze Y:", najwyzszy_element_Y)

# l) Usunięcie pierwszego elementu ze zbioru X i dołączenie go do zbioru Y
pierwszy_element_X = X.pop()
Y.add(pierwszy_element_X)
print("l) Usunięto pierwszy element z X i dodano do Y:")
print("   Zbiór X po usunięciu:", X)
print("   Zbiór Y po dodaniu:", Y)

# m) Przekopiowanie wszystkich elementów z X do Y
Y.update(X)
print("m) Przekopiowano wszystkie elementy z X do Y:")
print("   Zbiór X po przekopiowaniu:", X)
print("   Zbiór Y po przekopiowaniu:", Y)

# n) Wyczyszczenie obu zbiorów
X.clear()
Y.clear()
print("n) Oba zbiory zostały wyczyszczone.")