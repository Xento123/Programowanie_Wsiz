x=float(input("Podaj liczbę x: "))
y=float(input("Podaj liczbę y: "))
z=float(input("Podaj liczbę z: "))

if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y

print("Posortowane liczby: ", x, y, z )