import os
import datetime

# UTILITY
def cls():
    # Curata ecranul

    os.system('clear' if os.name == 'posix' else 'cls')


def create_time(timp,format):
    """ CREARE OBIECT DATETIME DIN input string, cu formatul precizat!"""
    try:
        x = datetime.datetime.strptime(timp,format)
    except ValueError:
        raise ValueError("Data introdusă este invalidă")
    else:
        return x


def citire(prompt,func=None):
    # Functie de citire cu verificare

    i = input(prompt).lower()
    if func is not None:
        try:
            i = func(i)
        except ValueError:
            print("Input Invalid")
        else:
            return i
    else:
        return i

def afisare_calatorii(pachete):

    """
    Functie de afișare a pachetelor dintr-o lista sau a inexistenței lor în cazul în care nu există
    :param pachete: lista pachete
    :return:
    """
    print("AFIȘARE PACHETE CĂLĂTORII:")
    if type(pachete) == list:
        for i in range(len(pachete)):
            pachet = pachete[i]
            sosire = pachet['data_sosire']
            plecare = pachet['data_plecare']
            locatie = pachet['locatie'].capitalize()
            pret = pachet['pret']
            print(f"{i}. Perioada {sosire.date()}-{plecare.date()} cu destinația {locatie} în Valoare de {pret} RON")
    else:
        print("Nu există Pachete de afișat ")


# Services


def validare(calatorie,a=None):
    """
    Validează O călătorie
    :param calatorie: Dictionar
    :param a: Lista cu călătorii
    :return: 0 sau 1 daca este validă
    """
    # Procesare locatie
    calatorie['locatie'] = calatorie['locatie'].lower()
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
            calatorie['data_sosire'] = datetime.datetime.strptime(calatorie['data_sosire'], df)
            calatorie['data_plecare'] = datetime.datetime.strptime(calatorie['data_plecare'], df)
        except ValueError:
            raise ValueError("Incorect data format, Must be DD-MM-YYYY")
        # Interval de timp pozitiv
        if calatorie['data_sosire'] > calatorie['data_plecare']:
            raise ValueError("Intervalul de timp introdus nu este valid!")
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


def SERVICE_sterge_pachet(a, locatie = None, durata = None, pret = None, ind = None):
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
            inceput = a[i]['data_sosire']
            sfarsit =  a[i]['data_plecare']
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
    elif ind is not None:
        del a[ind]
    return a


def SERVICE_cautare_interval_timp(a, inceput, sfarsit):
    """

    :param a: Lista pachete calatorii
    :param inceput: inceputul intervalului
    :param sfarsit: sfarsitul intervalului
    :return: lista cu pachetele de calatorie in intervalul specificat
    """
    lista = []
    for i in a:
        if (i['data_sosire'] - inceput).days <= 0 and (i['data_plecare'] - sfarsit).days >= 0:
            lista.append(i)

    return lista


def SERVICE_raport_destinatie(a,locatie):
    """

    :param a: Lista cu calatorii
    :param locatie: locatia de raportat
    :return: nr de pachete de calatorie
    """
    nr = 0
    lista = []
    for i in a:
        if i['locatie'] == locatie:

            nr += 1
            lista.append(i)
    return (nr, lista)


def SERVICE_filtrare_pret_locatie(a, pret, locatie):
    length = len(a)
    i = 0
    while i < length:
        if a[i]['pret'] > pret and a[i]['locatie'] != locatie:
            a = SERVICE_sterge_pachet(a, None, None, None, i)
            i -= 1
            length -= 1
        i+= 1


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
    q = citire(":").lower()
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
                afisare_calatorii(a)

            case "q":
                exit(0)

        print_main_menu()
        q = citire(":").lower()


def meniu_pachete(a):
    """
    Meniu Creare Pachete
    :param a: Lista pachete
    :return:
    """
    print_menu_pachete()
    q = citire(":").lower()
    while q != "q":
        match q:
            case "1":
                UI_creare_pachet(a)
                afisare_calatorii(a)
            case "2":
                UI_modifica_pachet(a)
                afisare_calatorii(a)
        print_menu_pachete()
        q = citire(":")
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
    locatie = input("Locație:").lower()
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
    locatie = input("Locație:").lower()
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
    q = citire(":").lower()
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
        afisare_calatorii(a)
        q = citire(":").lower()

    return a


def meniu_sterge_locatie(a):

    locatie = input("Introduceți Locatia pe care vreti să o eliminați:").lower()
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
    q = citire(":").lower()
    while q != "q":
        match q:
            case "1":
                lista = UI_cautare_interval_timp(a)
                afisare_calatorii(lista)
        print_menu_cautare()
        q = citire(":").lower()
    cls()



def UI_cautare_interval_timp(a):
    inceput = create_time(input("Data sosire (Zi Luna An) :"),'%d %m %Y')
    sfarsit = create_time(input("Data plecare (Zi Luna An :"),'%d %m %Y')
    return SERVICE_cautare_interval_timp(a, inceput, sfarsit)

def meniu_rapoarte(a):
    print_menu_rapoarte()
    q = citire(":").lower()
    while q != "q":
        match q:
            case "1":
                (nr, lista) = UI_rapoarte_destinatie(a)
                cls()
                print_menu_rapoarte()
                if nr:
                    print(f"Au fost găsite {nr} pachete:")
                    afisare_calatorii(lista)
                else:
                    print("Nu există nici un pachet pe locația aleasă")
        q = citire(":").lower()

def UI_rapoarte_destinatie(a):
    locatie = citire("Destinație: ").lower()
    return SERVICE_raport_destinatie(a, locatie)


def meniu_filtrare(a):
    print_menu_filtrare()
    q = citire(":").lower()
    while q != "q":
        match q:
            case "1":
                UI_filtrare_pret_locatie(a)
                cls()
                print_menu_filtrare()
                afisare_calatorii(a)
        q = citire(":").lower()

def UI_filtrare_pret_locatie(a):
    pret = citire("Prețul călătoriei: ", int)
    locatie = citire("Locația călătoriei: ")
    SERVICE_filtrare_pret_locatie(a, pret, locatie)

# Teste


def test_adauga_modifica():
    assert SERVICE_modifica_pachet([{'id':1}],{'id':1,'data_sosire':"25 04 2023",'data_plecare':"25 04 2024",'locatie':"belarus",'pret':150}) == True
    assert SERVICE_modifica_pachet([{'id':2}],{'id':1,'data_sosire':"25 04 2023",'data_plecare':"25 04 2024",'locatie':"belarus",'pret':150}) == False


def test_sterge():
    a = [{'id':1,'data_sosire':"25 04 2023",'data_plecare':"25 04 2024",'locatie':"belarus", 'pret':"1500"}]
    assert SERVICE_sterge_pachet(a,'belarus') == []
    assert SERVICE_sterge_pachet(a,None,400) == []
    assert  SERVICE_sterge_pachet(a,None,None,1500) == []
    assert SERVICE_sterge_pachet(a, 'Paris') == a
    assert SERVICE_sterge_pachet(a, None, 290) == a
    assert SERVICE_sterge_pachet(a, None, None, 1300) ==a
def test_validare():
    assert validare({'id':1,
                 'data_sosire':"25 04 2023",
                 'data_plecare':"25 04 2024",
                 'locatie':"belarus",
                 'pret':"1500"},[]) == True

    assert validare({'id': 1,
                         'data_sosire': "25 04 2023",
                         'data_plecare': "25 04 2024",
                         'locatie': "belarus",
                         'pret': "1500"}, [{'id': 1,
                         'data_sosire': "25 04 2023",
                         'data_plecare': "25 04 2024",
                         'locatie': "belarus",
                         'pret': "1500"}]) == False
    assert validare({'id': 1,
                         'data_sosire': "25 asdf 2023",
                         'data_plecare': "25 04 2024",
                         'locatie': "belarus",
                         'pret': "1500"},[]) == False
    assert validare( {'id': 'asdf',
                         'data_sosire': "25 asdf 2023",
                         'data_plecare': "25 04 2024",
                         'locatie': "belarus",
                         'pret': "1500"},[]) == False
    assert validare({'id': 1,
                     'data_sosire': "25 04 2023",
                     'data_plecare': "25 04 2022",
                     'locatie': "belarus",
                     'pret': "1500"}, []) == False


def test_creare_timp():
    assert(type(create_time("25 04 2004", "%d %m %Y"))) == datetime.datetime
    try:
        create_time("255 04 2004", "%d %m %Y")
        assert False
    except ValueError:
        assert True


def test_cautare_interval_timp():
    a = [{'id': 1,'data_sosire': create_time("25 04 2023","%d %m %Y"),'data_plecare': create_time("25 04 2024", "%d %m %Y"),'locatie': "belarus", 'pret': "1500"}]
    inceput = create_time("25 04 2023","%d %m %Y")
    sfarsit = create_time("25 04 2024", "%d %m %Y")
    assert SERVICE_cautare_interval_timp(a,inceput,sfarsit) == a
    inceput = create_time("25 04 2023", "%d %m %Y")
    sfarsit = create_time("25 05 2024", "%d %m %Y")
    assert SERVICE_cautare_interval_timp(a, inceput, sfarsit) == []


def test_raport_destinatie():
    a = [{'id': 1,'data_sosire': create_time("25 04 2023","%d %m %Y"),'data_plecare': create_time("25 04 2024", "%d %m %Y"),'locatie': "belarus", 'pret': "1500"}]
    assert SERVICE_raport_destinatie(a,"belarus") == (1, a)
    assert SERVICE_raport_destinatie(a, "Paris") == (0, [])


def test_filtrare():
    a = [{'id': 1, 'data_sosire': create_time("25 04 2023", "%d %m %Y"),'data_plecare': create_time("25 04 2024", "%d %m %Y"), 'locatie': "belarus", 'pret': 1500}]
    SERVICE_filtrare_pret_locatie(a, 1000, 'PARIS')
    assert a == []
    a = [{'id': 1, 'data_sosire': create_time("25 04 2023", "%d %m %Y"),'data_plecare': create_time("25 04 2024", "%d %m %Y"), 'locatie': "belarus", 'pret': 1500}]
    SERVICE_filtrare_pret_locatie(a, 3000, 'belarus')
    assert a != []


def run_tests():
    test_validare()
    test_adauga_modifica()
    test_sterge()
    test_creare_timp()
    test_cautare_interval_timp()
    test_raport_destinatie()
    test_filtrare()


def run():
    a = []
    run_tests()
    main_menu(a)


run()