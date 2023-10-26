from Service.crud import adauga_pachet_lista, SERVICE_modifica_pachet, stergere_pachete_destinatie, \
    stergere_pachete_data, stergere_pachete_pret
from Utility.utility import cls, citire_data, citire_nr
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
            sosire = datetime.datetime.strftime(pachet['data_sosire'],"%d.%m.%Y")
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
    data_sosire = citire_data("%d %m %Y","Ati introdus o data invalida.","Introduceți data de sosire(zi luna an): ")
    data_plecare = citire_data("%d %m %Y","Ati introdus o data invalida", "Introduceți data de plecare(zi luna an): ")
    locatie = input("Locatie:")
    pret = citire_nr("Introduce-ți pretul pachetului:",int,"Număr invalid")
    try:
        adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    except Exception as ex:
        print(ex)


def ui_modificare_pachet(pachete):
    id = citire_nr("ID:",int,"Id-ul trebuie sa fie un numar intreg")
    data_sosire = citire_data("%d %m %Y","Ati introdus o data invalida","Introduceți noua data de sosire(zi luna an):")
    data_plecare = citire_data("%d %m %Y","Ati introdus o data invalida","Introduceți noua data de plecare(zi luna an):")
    locatie = input("Locatia noua:")
    pret = citire_nr("Pretul nou:",int,"Pretul trebuie sa fie un numar intreg")
    SERVICE_modifica_pachet(pachete,id,data_sosire,data_plecare,locatie,pret)

def adaugare_pachet_menu(pachete):
    cls()
    while True:
        print_adaugare_pachet_menu()
        cmd = input(":").lower()
        match cmd:
            case '1':
                cls()
                #SERVICE ADAUGARE
                ui_adaugare_pachet(pachete)
            case '2':
                cls()
                #Service Modificare
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
    locatie = input("Locatie:")
    stergere_pachete_destinatie(pachete, locatie)


def UI_stergere_pachete_data(pachete):
    zile = citire_nr("Zile:",int,"Ziua trebuie sa fie un nr")
    stergere_pachete_data(pachete,zile)


def UI_stergere_pachete_pret(pachete):
    pret = citire_nr("Pret:", int, "Pretul trebuie sa fie un numar intreg")
    stergere_pachete_pret(pachete,pret)

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
                pass
            case '4':
                pass
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
