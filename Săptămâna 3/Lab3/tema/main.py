"""TEMĂ LABORATOR EXERCIȚIILE 1-4-13  """
# 6 PE DATA VIITOARE
import os


# UTILITY
def cls():
    # Curata ecranul
    os.system('clear' if os.name == 'posix' else 'cls')

# Menus


def print_menu():
    # Afișează Meniu Principal

    print("Meniu Aplicatie:")
    print("1. Creare Listă")
    print("2. Secventa de lungime maximă ce conține doar nr prime")
    print("3. Secvența de lungime maximă a cărei elemente au suma 5")
    print("4. Secventa Maximă Crescătoare")
    print("A. Afișează lista")
    print("Q. Ieșire")


def print_list_menu():
    # Afișează meniu pentru crearea listei

    print("Meniu Creare Listă")
    print("Q. exit")

# SERVICES
def is_prime(n):
    # Verifica daca nr este prim

    if n == 0 or n == 1:
        return False
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, n, 2):
        if i * i > n:
            break
        if n % i == 0:
            return False

    return True


def creare_lista(a):
    # Crează o listă cu numere întregi
    q = input(":").lower()
    while q != "q":

        if q.isnumeric():
            a.append(int(q))
        else:
            print("The input must be a int")
        q = input(":")
    return a


def secventa_prime(a):
    # Gaseste cea mai mare secventa de nr prime
    index_cur = -1
    index = -1
    longest = 0
    longest_cur = 0
    for i in range(len(a)):
        if is_prime(a[i]):
            if longest_cur == 0:
                index_cur = i
            longest_cur += 1

        else:
            if longest_cur > longest:
                longest = longest_cur
                index = index_cur
            longest_cur = 0
    if longest_cur > longest:
        longest = longest_cur
        index = index_cur

    return a[index:index+longest]


def secvente_suma5(a):
    # Gaseste cea mai mare secventa de nr cu suma lor 5
    longest_so_far = 0
    longest_cur = 0
    index_so_far = -1
    index_cur = -1
    for i in range(len(a)):
        suma = 0
        for j in range(i, len(a)):
            suma += a[j]
            if suma == 5:
                longest_cur = j-i+1
                index_cur = i

        if longest_cur > longest_so_far:
            longest_so_far = longest_cur
            index_so_far = index_cur
    return a[index_so_far:index_so_far+longest_so_far]


def sir_max(a):
    # Gaseste cea mai mare secventa de nr crescatoare
    longest_so_far = 1
    longest_cur = 1
    index_so_far = 0
    index_cur = -1
    for i in range(len(a)-1):
        j = i+1
        while j <= (len(a) -1) and a[j] > a[j-1]  :
            if longest_cur == 1:
                index_cur = i
            longest_cur+= 1
            j+=1


        if longest_cur > longest_so_far:
            longest_so_far = longest_cur
            index_so_far = index_cur
        longest_cur = 1
    return a[index_so_far:index_so_far + longest_so_far]


# Main
def run():
    a = []
    print_menu()
    q = input(":").lower()
    while q != "q":
        match q:
            case "1":
                cls()
                print_list_menu()
                creare_lista(a)
                cls()

            case "2":
                cls()
                b = secventa_prime(a)
                print(b)

            case "3":
                cls()
                b = secvente_suma5(a)
                print(b)
            case "4":
                cls()
                b = sir_max(a)
                print(b)

            case "a":
                print(a)

            case "q":
                exit(0)

        print_menu()
        q = input(":").lower()


# Teste
def test_is_prime():
    assert is_prime(2) == 1
    assert is_prime(19) == 1
    assert is_prime(9) == 0
    assert is_prime(1) == 0
    assert is_prime(0) == 0
    assert is_prime(4) == 0
    assert is_prime(-2) == 0
    assert is_prime(-4) == 0


def test_secventa_sum5():
    assert secvente_suma5([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
    assert secvente_suma5([1, 1, 5, 2, 1, 3]) == [5]
    assert secvente_suma5([3, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
    assert secvente_suma5([7, 7, 7, 7, 5]) == [5]
    assert secvente_suma5([5]) == [5]
    assert secvente_suma5([9, 9, 9, 9, 9]) == []
    assert secvente_suma5([0, 4, 0, 1, 0]) == [0, 4, 0, 1, 0]
    assert secvente_suma5([1, 1, 9, -4, 1]) == [9, -4]


def test_secventa_prime():
    assert secventa_prime([2, 3, 5, 7, 11]) == [2, 3, 5, 7, 11]
    assert secventa_prime([2, 3, 5, 6, 2, 3, 5, 7]) == [2, 3, 5, 7]
    assert secventa_prime([1, 0, 4, 6, 9]) == []
    assert secventa_prime([1, 0, 2]) == [2]


def test_sir_max():
    assert sir_max([5,22,35,45]) == [5,22,35,45]
    assert sir_max([5,4,3,2,1]) == [5]
    assert sir_max([5,6,7,3,4,5,6]) == [3,4,5,6]
    assert sir_max([0,0,0,0,0]) == [0]


def run_test():
    test_is_prime()
    test_secventa_sum5()
    test_secventa_prime()
    test_sir_max()

run_test()
run()
