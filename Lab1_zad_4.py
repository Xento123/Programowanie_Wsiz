import math
print("Równanie w postaci a*x^2 + bx + c == 0")
a = float(input("podaj a:"))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))
delta = b**2 - 4 * a * c
if delta > 0:
    print("Pierwiastki równania kwadratowego: ")
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print("x1: ", x1)
    print("x2: ", x2)
elif delta == 0:
    print("Pierwiastek podwójny równania: ")
    x0 = -b / (2 * a)
    print("x0: ", x0)
else:
    print("Delta jest ujemna, wiec nie liczymy miejsc zerowych.")
