from Service.Services import undo
from UI.meniu_adaugari import adaugare_pachet_menu
from UI.meniu_cautari import cautare_pachet_menu
from UI.meniu_filtrare import filtrare_pachete_menu
from UI.meniu_rapoarte import rapoarte_pachete_menu
from UI.meniu_stergeri import stergere_pachet_menu
from Utility.utility import cls, afisare_calatorii


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


def main_menu(pachete,undo_list):
    cls()
    print_main_menu()
    while True:

        cmd = input(":").lower()
        match cmd:
            case '1':
                cls()
                adaugare_pachet_menu(pachete, undo_list)
                print_main_menu()
            case '2':
                cls()
                stergere_pachet_menu(pachete, undo_list)
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
                cls()
                filtrare_pachete_menu(pachete, undo_list)
                print_main_menu()
            case '6':
                pachete = undo(pachete, undo_list)
                cls()
                print_main_menu()
                afisare_calatorii(pachete)
            case 'a':
                cls()
                print_main_menu()
                afisare_calatorii(pachete)
            case 'q':
                exit(0)
