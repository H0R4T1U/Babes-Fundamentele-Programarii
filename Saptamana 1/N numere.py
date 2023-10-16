sum = 0
n = int(input("baga nr:"))
for i in range(n):
    x = int(input(f"Nr {i+1} pt suma: "))
    if x >= 0:
        sum += x
    else:
        print("Nr nu este natural !")

print(f"suma este {sum}")
