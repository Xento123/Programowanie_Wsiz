a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

if a < b:
    while a <= b:
        if a % 2 == 0:
            print(a)
        a += 1
elif a == b:
    print("Liczby są równe")
else:
    while b <= a:
        if b % 2 == 0:
            print(b)
        b += 1