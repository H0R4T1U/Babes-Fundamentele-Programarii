'''
Acest algoritm demonstreaza conjectura lui goldbach care atestă că orice număr par
mai mare ca și 2 poate fi scris ca si sumă de 2 numere prime. S-a dovedit totuși că
nr: 3 325 581 707 333 960 528(cvintilioane) este cel mai mic număr par ce nu respectă
această regulă

În algoritm am folosit ciurul lui eratosthenes să generez toate numerele prime < n
apoi am parcurs vectorul si am scazut fiecare nr prim din n iar dacă diferența rezultată
este și ea primă returnăm numerele.
8 -> 3,5

'''

def create_sieve(l,n):
    for i in range(n):
        l.append(0)
    l[0] = 1
    l[1] = 1
    for i in range(2,n):
        j = 2
        while i * j < n:
            l[i*j] = 1
            j+= 1

print("Numărul introdus trebuie să fie par și mai mare ca 2")

n = int(input("Introdu numărul: "))
l = []

if n == 2 or n % 2 == 1:
    print("Numărul introdus nu este valid!")
else:
    create_sieve(l,n)
    for i in range(len(l)):
        n2 = n-i
        if l[i] == 0 and l[n2] == 0:
            print(f"Suma numerelor prime {i} și {n2} este egala cu {n} !")
            break
