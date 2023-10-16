'''
Porblema 3
Daca introducem 2004 si 61 trebuie sa returneze 1 martie
daca introducem 2005 si 61 trebuie sa returneze 2 martie
'''
import datetime

an = int(input("introdu anul:"))
nr_ordine = int(input("Introdu numărul de ordine a zilei:"))
curent = datetime.datetime.now()
an_curent = curent.year

if an > an_curent:
    print("Anul introdus nu este valid")
    exit(0)
if nr_ordine > 366:
    print("Nr de ordine al zilei nu este valid")
    exit(0)
if nr_ordine == 366 and an % 4 != 0:
    print("Datele de intrare nu sunt valide!")
    exit(0)

inceput_an = datetime.date(an,1,1) + datetime.timedelta(nr_ordine-1)
if inceput_an.year == curent.year and inceput_an.month > curent.month:
    print("Nu am ajuns inca la aceasta ziua")
    exit(0)
if inceput_an.year == curent.year and inceput_an.month == curent.month and inceput_an.day > curent.day:
    print("Nu am ajuns inca la aceasta zi")
print(inceput_an)
