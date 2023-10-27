from Repositories.pachetCRUD import get_data_sosire, get_data_plecare, get_locatie, get_pret, sterge_pachet, get_id
from Utility.utility import quick_sort_pret


def cautare_pachete_interval(pachete, inceput, sfarsit):
    """
    Tipărirea pachetelor de călătorie care presupun un sejur într-un
    interval dat
    :param pachete: pachete
    :param inceput: inceputul intervalului
    :param sfarsit: sfarsitul intervalului
    :return: Lista de pachete ce indeplinesc conditia data
    """
    afisare = []
    for pachet in pachete:
        data_sosire = get_data_sosire(pachet)
        data_plecare = get_data_plecare(pachet)
        if (data_sosire - inceput).days <= 0 <= (data_plecare - sfarsit).days:
            afisare.append(pachet)

    return afisare


def cautare_pachete_dest_pret(pachete, destinatie, pret):
    """
    Tipărirea pachetelor de călătorie cu o destinație dată și cu preț mai
    mic decât o sumă dată
    :param pachete: pachete
    :param destinatie: destinatie
    :param pret: pret
    :return: lista de pachete ce indeplinesc cerinta
    """
    afisare = []
    for pachet in pachete:
        if get_locatie(pachet) == destinatie and get_pret(pachet) < pret:
            afisare.append(pachet)

    return afisare


def cautare_pachete_sfarsit(pachete, sfarsit):
    """
    Tipărirea pachetelor de călătorie cu o anumită dată de sfârși
    :param pachete: Pachete
    :param sfarsit: Data de plecare
    :return: lista cu pachete care indeplinesc conditia
    """
    afisare = []
    for pachet in pachete:
        if get_data_plecare(pachet) == sfarsit:
            afisare.append(pachet)

    return afisare


def raport_oferte_destinatie(pachete, locatie):
    """
    Functie ce gaseste nr de oferte dintr-o anumită locație
    :param pachete: lista pachete
    :param locatie: locatia
    :return: Nr de pachete ce respectă această condiție cât și ofertele
    """
    afisare = []

    for pachet in pachete:
        if get_locatie(pachet) == locatie:
            afisare.append(pachet)

    return afisare


def raport_oferte_interval_cresc(pachete, inceput, sfarsit):
    """
    Functie de gasire a ofertelor din interval si a returnarii lor in ordine crescatoare
    :param pachete: lista pachete
    :param inceput: inceput interval timp
    :param sfarsit: sfarsit interval timp
    :return: lista de afisat cu pachetele ordonate crescator
    """
    pachete_interval = cautare_pachete_interval(pachete, inceput, sfarsit)
    quick_sort_pret(pachete_interval, 0, len(pachete_interval)-1)
    return pachete_interval


def raport_medie_pret_dest(pachete, destinatie):
    suma = 0
    nr = 0
    for pachet in pachete:
        if get_locatie(pachet) == destinatie:
            nr += 1
            suma += get_pret(pachet)

    return suma/nr

def filtrare_pret_destinatie(pachete, destinatie, pret):
    """
    Elimina ofertele ce au un pret mai mare decat cel dat si o destinatie diferita
    :param pachete: lista pachete
    :param destinatie:destinatia data
    :param pret: pret
    :return: Nr de pachete eliminate
    """
    i = 0
    length = len(pachete)
    while i < length:
        pachet = pachete[i]
        if get_locatie(pachet) != destinatie and get_pret(pachet) > pret:
            sterge_pachet(pachete, get_id(pachet))
            i -= 1
            length -= 1
        i += 1

