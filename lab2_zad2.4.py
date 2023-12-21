n = int(input("Podaj liczbę naturalną n: "))
a = float(input("Podaj pierwszy element ciągu: "))
r = float(input("Podaj różnicę ciągu (r): "))

print("Pierwsze", n, "elementy ciągu arytmetycznego:")
for i in range(n):
    element = a + i * r
    print(element)