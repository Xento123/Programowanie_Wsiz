zakupy = {
    'jajka': 5.50,
    'chleb': 2.20,
    'mleko': 3.00,
    'ser': 4.50,
    'kawa': 8.90
}

print("Lista zakupów:")
for artykul, kwota in zakupy.items():
    print(f"{artykul}: {kwota} zł")

suma=sum(zakupy.values())
print("Suma zakupów wynosi:",suma)