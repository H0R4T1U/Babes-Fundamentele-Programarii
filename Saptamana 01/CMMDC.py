a = int(input("A= "))
b = int(input("B= "))
if a >= 0 and b >= 0:
    while b != 0:
        c = a % b
        a = b
        b = c
print(f"Cel mai mare divizor comun al celor 2 nr este {a}")
