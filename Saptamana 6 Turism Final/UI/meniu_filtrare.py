from Service.Services import filtrare_pret_destinatie, filtrare_luna
from Utility.utility import citire_nr, cls


def print_menu_filtrare():
    print("Meniu Filtrare")
    print("1. Filtrare oferte cu pret mai mare si locție diferită")
    print("2. Filtrare oferte după lună")
    print("Q. Back")


def Ui_filtrare_pret_destinatie(pachete, undo_list):
    pret = citire_nr("Pret:", int, "pretul introdus nu este valid")
    locatie = input("Locatie:").lower()
    return filtrare_pret_destinatie(pachete, locatie, pret, undo_list)


def UI_filtrare_luna(pachete, undo_list):
    luna = citire_nr("Luna:", int, "Luna introdusă nu este validă")
    while luna > 12:
        luna = citire_nr("Luna:", int, "Luna introdusă nu este validă")
    return filtrare_luna(pachete, luna, undo_list)


def filtrare_pachete_menu(pachete, undo_list):
    print_menu_filtrare()
    while True:
        cmd = input(":").lower()
        match cmd:
            case "1":
                cls()
                sterse = Ui_filtrare_pret_destinatie(pachete, undo_list)
                print_menu_filtrare()
                print(f"Au fost șterse {sterse} pachete")
            case "2":
                cls()
                sterse = UI_filtrare_luna(pachete, undo_list)
                print_menu_filtrare()
                print(f"Au fost șterse {sterse} pachete")
            case "q":
                break
