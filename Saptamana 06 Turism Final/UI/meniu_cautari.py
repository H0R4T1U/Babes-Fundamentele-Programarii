from Service.Services import cautare_pachete_interval, cautare_pachete_dest_pret, cautare_pachete_sfarsit
from Utility.utility import cls, afisare_calatorii, citire_data, valideaza_interval, citire_nr


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
    destinatie = input("Destinație:").lower()
    pret = citire_nr("Preț:", int, "Nr trebuie să fie întreg pozitiv")
    return cautare_pachete_dest_pret(pachete, destinatie, pret)


def UI_cautare_pachete_sfarsit(pachete):
    sfarsit = citire_data("%d %m %Y", "Data introdusă nu este validă",
                          "Introduceți data de sfărșit a călătoriei(zi luna an):")
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
