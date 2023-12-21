def funkcja_kwadratowa(x):
    return 2 * x**2 - 5 * x - 8

x_start=-4
x_stop=4
krok=0.5

print("x\t\t y")
print("--------------------")
x = x_start
while x <= x_stop:
    y = funkcja_kwadratowa(x)
    print(f"{x:.2f}\t\t{y:.2f}")
    x += krok