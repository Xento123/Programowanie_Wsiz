# a) Definicja słownika rachunków za prąd
rachunki_prad = {
    'styczeń': 150.50,
    'luty': 120.30,
    'marzec': 180.80,
    'kwiecień': 160.00,
    'maj': 200.25
}
wartosci = list(rachunki_prad.values())
maksymalna_wartosc = max(wartosci)
minimalna_wartosc = min(wartosci)
suma_wartosci = sum(wartosci)
srednia_wartosc = suma_wartosci / len(wartosci)

print("a) Maksymalna wartość:", maksymalna_wartosc)
print("   Minimalna wartość:", minimalna_wartosc)
print("   Suma wartości:", suma_wartosci)
print("   Średnia wartość:", srednia_wartosc)

# b) Sprawdzenie, czy ostatni miesiąc przekroczył średnią
ostatni_miesiac = list(rachunki_prad.keys())[-1]
wartosc_ostatniego_miesiaca = rachunki_prad[ostatni_miesiac]

if wartosc_ostatniego_miesiaca > srednia_wartosc:
    print("b) Zacznij oszczędzać")
else:
    print("b) Jesteś bezpieczny")