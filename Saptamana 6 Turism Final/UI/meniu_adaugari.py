from Service.crud import adauga_pachet_lista, SERVICE_modifica_pachet
from Utility.utility import citire_data, citire_nr, cls


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
