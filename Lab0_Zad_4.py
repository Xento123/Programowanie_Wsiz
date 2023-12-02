import random

#droga=int(input("Podaj długość trasy: "))
droga=random.randint(1,1000)
print("Trasa: ",droga)

spalanie=float(input("Podaj spalanie twojego samochodu"))
cena=6.50

zuzycie=(droga*spalanie)/100
koszty=zuzycie*cena

#print("Zuzyjesz: ", zuzycie, "litrów paliwa, za które zapłacisz ",koszty, "złotych")

print(f"Zużyjesz {zuzycie} litrów paliwa, za które zapłacisz {koszty} złotych")

