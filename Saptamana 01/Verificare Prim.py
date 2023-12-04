import math

n = int(input("Introdu nr: "))
flag = 0
if(n == 0 or n == 1):
    flag = 1
if( n % 2 == 0 and n != 2):
    flag = 1

for i in range(3,int(math.sqrt(n)),2):
    if(n % i == 0):
        flag = 1

if flag:
        print(f"Nr {n} nu este prim")
else:
    print(f"Nr {n} este prim ")
