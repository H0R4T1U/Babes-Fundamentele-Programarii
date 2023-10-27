from Service.Services import cautare_pachete_interval, raport_oferte_destinatie, raport_oferte_interval_cresc, \
    raport_medie_pret_dest, cautare_pachete_dest_pret, cautare_pachete_sfarsit
from Service.crud import adauga_pachet_lista, SERVICE_modifica_pachet, stergere_pachete_destinatie, \
    stergere_pachete_data, stergere_pachete_pret
from Utility.utility import cls, citire_data, citire_nr, valideaza_interval
import datetime


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
            id = pachet['id']
            sosire = datetime.datetime.strftime(pachet['data_sosire'], "%d.%m.%Y")
            plecare = datetime.datetime.strftime(pachet['data_plecare'], "%d.%m.%Y")
            locatie = pachet['locatie'].capitalize()
            pret = pachet['pret']
            print(f"{id}. Perioada de la: {sosire} pana la: {plecare} cu destinația {locatie} în Valoare de {pret} RON")
    else:
        print("Nu există Pachete de afișat ")


def print_adaugare_pachet_menu():
    print("1. Adaugă pachet")
    print("2. Modifică pachet")
    print("Q. Ieșire")


def ui_adaugare_pachet(pachete):
    data_sosire = citire_data("%d %m %Y", "Ati introdus o data invalida.", "Introduceți data de sosire(zi luna an): ")
    data_plecare = citire_data("%d %m %Y", "Ati introdus o data invalida", "Introduceți data de plecare(zi luna an): ")
    locatie = input("Locatie:").lower()
    pret = citire_nr("Introduce-ți pretul pachetului:", int, "Număr invalid")
    try:
        adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    except Exception as ex:
        print(ex)


def ui_modificare_pachet(pachete):
    id = citire_nr("ID:", int, "Id-ul trebuie sa fie un numar intreg")
    data_sosire = citire_data("%d %m %Y", "Ati introdus o data invalida",
                              "Introduceți noua data de sosire(zi luna an):")
    data_plecare = citire_data("%d %m %Y", "Ati introdus o data invalida",
                               "Introduceți noua data de plecare(zi luna an):")
    locatie = input("Locatia noua:").lower()
    pret = citire_nr("Pretul nou:", int, "Pretul trebuie sa fie un numar intreg")
    SERVICE_modifica_pachet(pachete, id, data_sosire, data_plecare, locatie, pret)


def adaugare_pachet_menu(pachete):
    cls()
    while True:
        print_adaugare_pachet_menu()
        cmd = input(":").lower()
        match cmd:
            case '1':
                cls()
                # SERVICE ADAUGARE
                ui_adaugare_pachet(pachete)
            case '2':
                cls()
                # Service Modificare
                ui_modificare_pachet(pachete)
                pass
            case 'q':
                break


def print_main_menu():
    print("Meniu Pachete de călătorii:")
    print("1. Adăugare/Modificare Pachete")
    print("2. Ștergere Pachete")
    print("3. Căutare Pachete")
    print("4. Raportare Pachete")
    print("5. Filtrare Pachete")
    print("6. Undo")
    print("A. Afișare Pachete")
    print("Q. Exit")


def print_menu_stergeri():
    print("Meniu stergeri")
    print("1. Stergere pachete prin locatie")
    print("2. Stergere pachete cu mai putin de n zile")
    print("3. Stergere pachete cu pretul mai scump de x")
    print("q. Back")


def UI_stergere_pachet_locatie(pachete):
    locatie = input("Locatie:").lower()
    stergere_pachete_destinatie(pachete, locatie)


def UI_stergere_pachete_data(pachete):
    zile = citire_nr("Zile:", int, "Ziua trebuie sa fie un nr")
    stergere_pachete_data(pachete, zile)


def UI_stergere_pachete_pret(pachete):
    pret = citire_nr("Pret:", int, "Pretul trebuie sa fie un numar intreg")
    stergere_pachete_pret(pachete, pret)


def stergere_pachet_menu(pachete):
    print_menu_stergeri()
    while True:
        cmd = input(":").lower()
        match cmd:
            case '1':
                cls()
                UI_stergere_pachet_locatie(pachete)
                print_menu_stergeri()
            case '2':
                cls()
                UI_stergere_pachete_data(pachete)
                print_menu_stergeri()
            case '3':
                cls()
                UI_stergere_pachete_pret(pachete)
                print_menu_stergeri()
            case 'q':
                break


def print_menu_cautare():
    print("Meniu Căutare")
    print("1. Cautare pachete interval")
    print("2. Cautare pachete destinatie data si suma mai mica decat cea data")
    print("3. Cautare pachete cu o anumită dată de sfărșit")
    print("Q. Back")


def UI_cautare_pachet_interval(pachete):
    flag = 0
    while not flag:
        data_inceput = citire_data("%d %m %Y", "Data invalidă", "Introduceți data de inceput (zi luna an):")
        data_sfarsit = citire_data("%d %m %Y", "Data invalidă", "Introduceți data de sfarsit (zi luna an):")
        try:
            valideaza_interval(data_inceput, data_sfarsit)
        except Exception as ex:
            print(ex)
        else:
            return cautare_pachete_interval(pachete, data_inceput, data_sfarsit)


def UI_cautare_pachete_dest_pret(pachete):
    destinatie = input("Destinație").lower()
    pret = citire_nr("Preț", int, "Nr trebuie să fie întreg pozitiv")
    return cautare_pachete_dest_pret(pachete, destinatie, pret)


def UI_cautare_pachete_sfarsit(pachete):
    sfarsit = citire_data("%d %m %Y","Data introdusă nu este validă","Introduceți data de sfărșit a călătoriei(zi luna an):" )
    return cautare_pachete_sfarsit(pachete, sfarsit)


def cautare_pachet_menu(pachete):
    print_menu_cautare()
    while True:
        cmd = input(":").lower()
        match cmd:
            case '1':
                cls()
                afisare = UI_cautare_pachet_interval(pachete)
                print_menu_cautare()
                afisare_calatorii(afisare)
            case '2':
                cls()
                afisare = UI_cautare_pachete_dest_pret(pachete)
                print_menu_cautare()
                afisare_calatorii(afisare)
            case '3':
                cls()
                afisare = UI_cautare_pachete_sfarsit(pachete)
                print_menu_cautare()
                afisare_calatorii(afisare)
            case 'q':
                break


def print_menu_rapoarte():
    print("Meniu Afișare")
    print("1. Raport număr oferte destinație")
    print("2. Raport pachete disponibile intr-o perioada crescător dupa pret")
    print("3. Raport Medie Preț locație")
    print("Q. Back")


def UI_raport_oferte_destinatie(pachete):
    destinatie = input("Destinație:").lower()
    return raport_oferte_destinatie(pachete, destinatie)


def UI_raport_oferte_interval_cresc(pachete):
    flag = 0
    while not flag:
        data_inceput = citire_data("%d %m %Y", "Data invalidă", "Introduceți data de inceput (zi luna an):")
        data_sfarsit = citire_data("%d %m %Y", "Data invalidă", "Introduceți data de sfarsit (zi luna an):")
        try:
            valideaza_interval(data_inceput, data_sfarsit)
        except Exception as ex:
            print(ex)
        else:
            return raport_oferte_interval_cresc(pachete, data_inceput, data_sfarsit)


def UI_raport_medie_pret_dest(pachete):
    locatie = input("Locatie:").lower()
    return raport_medie_pret_dest(pachete, locatie)


def rapoarte_pachete_menu(pachete):
    cls()
    print_menu_rapoarte()
    while True:
        cmd = input(":").lower()
        match cmd:
            case "1":
                cls()
                afisare = UI_raport_oferte_destinatie(pachete)
                print_menu_rapoarte()
                print(f"S-au găsit {len(afisare)} oferte!")
                afisare_calatorii(afisare)
            case "2":
                cls()
                afisare = UI_raport_oferte_interval_cresc(pachete)
                print_menu_rapoarte()
                afisare_calatorii(afisare)
            case "3":
                cls()
                medie = UI_raport_medie_pret_dest(pachete)
                print_menu_rapoarte()
                print(f"Media de preț a pachetelor din locația selectată este {medie}")
            case "q":
                break



def main_menu(pachete):
    cls()
    print_main_menu()
    while True:

        cmd = input(":").lower()
        match cmd:
            case '1':
                cls()
                adaugare_pachet_menu(pachete)
                print_main_menu()
            case '2':
                cls()
                stergere_pachet_menu(pachete)
                print_main_menu()
            case '3':
                cls()
                cautare_pachet_menu(pachete)
                print_main_menu()
            case '4':
                cls()
                rapoarte_pachete_menu(pachete)
                print_main_menu()
            case '5':
                pass
            case '6':
                pass
            case 'a':
                cls()
                print_main_menu()
                afisare_calatorii(pachete)
            case 'q':
                exit(0)
