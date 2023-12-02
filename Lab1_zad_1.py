x=int(input("Podaj swój wiek"))

if x > 18:
    print("Cena biletu wynosi 20zł")
elif x < 0:
    print("Za mała liczba")
elif x >= 4:
    print("Cena biletu wynosi 10zł")
else:
    print("Bilet jest darmowy")