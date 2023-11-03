from Service.Services import raport_oferte_destinatie, raport_oferte_interval_cresc, raport_medie_pret_dest
from Utility.utility import citire_data, valideaza_interval, cls, afisare_calatorii


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

