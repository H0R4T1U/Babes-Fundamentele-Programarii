import os
import datetime

# UTILITY
def cls():
    # Curata ecranul

    os.system('clear' if os.name == 'posix' else 'cls')


def create_time(timp,format):

    return datetime.datetime.strptime(timp,format)


def citire(prompt,func=None):
    # Functie de citire cu verificare

    i = input(prompt)
    if func is not None:
        try:
            i = func(i)
        except ValueError:
            print("Input Invalid")
        else:
            return i
    else:
        return i
# Services


def validare(calatorie,a=None):
    """
    Validează O călătorie
    :param calatorie: Dictionar
    :param a: Lista cu călătorii
    :return: 0 sau 1 daca este validă
    """
    # Validare ID
    try:
        try:
            int(calatorie['id'])
        except ValueError:
            raise ValueError("ID was not a valid number!")
        if a is not None:
            for i in a:
                if i['id'] == calatorie['id']:
                    raise ValueError("ID Already Exist!")

        # Validare Data
        df = '%d %m %Y'
        try:
            datetime.datetime.strptime(calatorie['data_sosire'], df)
            datetime.datetime.strptime(calatorie['data_plecare'],df)
        except ValueError:
            raise ValueError("Incorect data format, Must be DD-MM-YYYY")
        # Validare Pret
        try:
            calatorie['pret'] = int(calatorie['pret'])
        except ValueError:
            raise ValueError("Prețul trebuie să fie un număr")
    except ValueError:
        return False
    else:
        return True


def SERVICE_creare_pachet(a,calatorie):
    """

    :param a: Lista calatorii
    :param calatorie: Calatoria ce urmează sa fie adăugată
    :return:
    """
    if validare(calatorie,a):
        a.append(calatorie)
    else:
        print("Invalid Input")


def SERVICE_modifica_pachet(a,calatorie):
    """
    Modifica o calatorie deja existenta
    :param a: lista calatorii
    :param calatorie: dictionar calatorie
    :return:
    """
    try:
        flag = 0
        if validare(calatorie):
            for i in range(len(a)):
                if a[i]['id'] == calatorie['id']:
                    flag = 1
                    a[i] = calatorie
            if flag == 0:
                raise ValueError("Id doesn't exist!")
        else:
            raise ValueError("Invalid Input")
    except ValueError:
        return False
    else:
        return True


def SERVICE_sterge_pachet(a, locatie = None, durata = None, pret = None):
    """

    :param a: Lista cu calatorii
    :param locatie: daca exista se vor sterge doar calatoriile dintr-o anumita locatie
    :param durata: daca exista se vor sterge doar calatoriile dintr-o anumita perioada de timp
    :param pret: daca exista se vor sterge doar calatoriile ce au un anumit pret
    :return: Lista modificata
    """
    to_delete = []
    if locatie is not None:
        for i in range(len(a)):
            if a[i]['locatie'] == locatie:
                to_delete.append(i)
        start = len(to_delete)
        for i in range(start):
            index = to_delete[i]
            del a[index - i]
        # sterge pachetele care contin o anumita locatie
    elif durata is not None:
        to_delete = []
        for i in range(len(a)):
            inceput = create_time(a[i]['data_sosire'],"%d %m %Y")
            sfarsit = create_time(a[i]['data_plecare'],"%d %m %Y")
            delta = sfarsit - inceput
            if delta.days < durata:
                to_delete.append(i)
        start = len(to_delete)
        for i in range(start):
            index = to_delete[i]
            del a[index - i]
        # sterge parchetele care sunt intr-un anumit interval de timp
    elif pret is not None:
        for i in range(len(a)):
            if a[i]['pret'] == pret:
                to_delete.append(i)
        start = len(to_delete)
        for i in range(start):
            index = to_delete[i]
            del a[index - i]

        # sterge pachetele ce au un anumit pret.
    return a


# Menus && UI

def print_main_menu():

    print("1. Pachete de călătorie ")
    print("2. Stergeri ")
    print("3. Căutare ")
    print("4. Rapoarte ")
    print("5. Filtrare ")
    print("Q. Ieșire ")


def print_menu_pachete():

    print("1. Adaugă Pachet de Călătorie")
    print("2. Modifică Pachet de Călătorie")
    print("Q. Ieșire ")


def print_menu_stergeri():
    print("1. Șterge Pachete dintr-o Destinație")
    print("2. Șterge Pachete cu o durată mai scurtă ca x")
    print("3. Șterge Pachetele cu suma x")
    print("Q. Ieșire ")


def print_menu_cautare():

    print("1. Căutare pachete dintr-un interval de timp")
    print("Q. Ieșire ")


def print_menu_rapoarte():

    print("1. Raport Oferte dintr-o destinație")
    print("Q. Ieșire ")


def print_menu_filtrare():

    print("1. Elimină oferte dintr-un interval")
    print("Q. Ieșire ")


def main_menu(a):
    """
    Meniul Principal al aplicatiei
    :param a: lista de calatorii
    :return:
    """
    a = []
    print_main_menu()
    q = input(":").lower()
    while q != "q":
        match q:
            case "1":
                cls()
                meniu_pachete(a)
                cls()

            case "2":
                cls()
                meniu_stergeri(a)
                cls()
            case "3":
                cls()
                meniu_cautare(a)
                cls()
            case "4":
                cls()
                meniu_rapoarte(a)
                cls()
            case "5":
                cls()
                meniu_filtrare(a)
                cls()
            case "a":
                print(a)

            case "q":
                exit(0)

        print_main_menu()
        q = input(":").lower()


def meniu_pachete(a):
    """
    Meniu Creare Pachete
    :param a: Lista pachete
    :return:
    """
    print_menu_pachete()
    q = input(":").lower()
    while q != "q":
        match q:
            case "1":
                UI_creare_pachet(a)
                print(f"Dictionaries: {a}")
            case "2":
                UI_modifica_pachet(a)
                print(f"Dictionaries: {a}")
        print_menu_pachete()
        q = input(":")
        cls()
    return a


def UI_creare_pachet(a):
    """

    :param a: Lista cu pachete
    :return:
    """
    id = input("ID:")
    data_sosire = input("Data Sosire (Zi Luna An):")
    data_plecare = input("Data plecare (Zi Luna An:")
    locatie = input("Locație:")
    pret = input("Preț:")
    calatorie = {'id': id,
                 'data_sosire': data_sosire,
                 'data_plecare': data_plecare,
                 'locatie': locatie,
                 'pret': pret}
    SERVICE_creare_pachet(a, calatorie)


def UI_modifica_pachet(a):
    """Creare Pachete"""

    id = input("ID:")
    data_sosire = input("Noua Data Sosire (Zi Luna An):")
    data_plecare = input("Data plecare (Zi Luna An:")
    locatie = input("Locație:")
    pret = input("Preț:")
    calatorie = {'id': id,
                 'data_sosire': data_sosire,
                 'data_plecare': data_plecare,
                 'locatie': locatie,
                 'pret': pret}
    SERVICE_modifica_pachet(a, calatorie)


def meniu_stergeri(a):
    """
    Meniu stergere pachete
    :param a: Lista cu pachete
    :return:
    """
    print_menu_stergeri()
    q = input(":").lower()
    while q != "q":
        match q:
            case "1":
                cls()
                meniu_sterge_locatie(a)
            case "2":
                meniu_sterge_interval(a)
            case "3":
                meniu_sterge_pret(a)
        print_menu_stergeri()
        print(a)
        q = input(":").lower()

    return a


def meniu_sterge_locatie(a):

    locatie = input("Introduceți Locatia pe care vreti să o eliminați:")
    a = SERVICE_sterge_pachet(a, locatie)


def meniu_sterge_interval(a):

    print("Programul va elimina toate pachetele de calatorie cu durata mai scurta decat cea precizata")
    interval = citire("Nr de zile:", int)

    a = SERVICE_sterge_pachet(a,None, interval)


def meniu_sterge_pret(a):
    pret = citire("Pret:", int)

    a = SERVICE_sterge_pachet(a,None,None, pret)
    return

def meniu_cautare(a):

    print_menu_cautare()
    q = input(":").lower()
    while q != "q":
        match q:
            case "1":
                break


def meniu_rapoarte(a):
    print_menu_rapoarte()
    q = input(":").lower()
    while q != "q":
        match q:
            case "1":
                break


def meniu_filtrare(a):
    print_menu_filtrare()
    q = input(":").lower()
    while q != "q":
        match q:
            case "1":
                break


# Teste


def test_adauga_modifica():
    assert SERVICE_modifica_pachet([{'id':1}],{'id':1,'data_sosire':"25 04 2023",'data_plecare':"25 04 2024",'locatie':"belarus",'pret':150}) == True
    assert SERVICE_modifica_pachet([{'id':2}],{'id':1,'data_sosire':"25 04 2023",'data_plecare':"25 04 2024",'locatie':"belarus",'pret':150}) == False


def test_sterge():
    a = [{'id':1,'data_sosire':"25 04 2023",'data_plecare':"25 04 2024",'locatie':"Belarus", 'pret':"1500"}]
    assert SERVICE_sterge_pachet(a,'Belarus') == []
    assert SERVICE_sterge_pachet(a,None,400) == []
    assert  SERVICE_sterge_pachet(a,None,None,1500) == []
    assert SERVICE_sterge_pachet(a, 'Paris') == a
    assert SERVICE_sterge_pachet(a, None, 290) == a
    assert SERVICE_sterge_pachet(a, None, None, 1300) ==a
def test_validare():
    assert validare({'id':1,
                 'data_sosire':"25 04 2023",
                 'data_plecare':"25 04 2024",
                 'locatie':"Belarus",
                 'pret':"1500"},[]) == True

    assert validare({'id': 1,
                         'data_sosire': "25 04 2023",
                         'data_plecare': "25 04 2024",
                         'locatie': "Belarus",
                         'pret': "1500"}, [{'id': 1,
                         'data_sosire': "25 04 2023",
                         'data_plecare': "25 04 2024",
                         'locatie': "Belarus",
                         'pret': "1500"}]) == False
    assert validare({'id': 1,
                         'data_sosire': "25 asdf 2023",
                         'data_plecare': "25 04 2024",
                         'locatie': "Belarus",
                         'pret': "1500"},[]) == False
    assert validare( {'id': 'asdf',
                         'data_sosire': "25 asdf 2023",
                         'data_plecare': "25 04 2024",
                         'locatie': "Belarus",
                         'pret': "1500"},[]) == False


def run_tests():
    test_validare()
    test_adauga_modifica()
    test_sterge()


def run():
    a = []
    run_tests()
    main_menu(a)


run()