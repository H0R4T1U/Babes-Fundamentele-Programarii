import datetime
import os

from Repositories.pachetCRUD import get_pret, get_data_sosire, get_id, get_locatie, get_data_plecare


def cls():
    """
    Sterge ecranul
    :return:
    """
    os.system('clear' if os.name == 'posix' else 'cls')


def citire_nr(prompt, f, msg):
    """
    Citeste un nr si il returneaza ca si int
    :param prompt: Ce se afiseaza
    :param f: functia de convertire
    :param msg: error msg
    :return:
    """
    while True:
        try:
            nr = f(input(prompt))
            if nr > 0:
                return nr
            else:
                raise ValueError
        except ValueError:
            print(msg)


def citire_data(format, msg, prompt="Introduceți data(zi luna an): "):
    """
    Citeste un data object
    :param format: formatul sau
    :param msg: mesajul de afisat in caz de eroare
    :param prompt: mesajul din prompt input
    :return: dataobject
    """
    while True:
        try:
            return datetime.datetime.strptime(input(prompt), format)
        except ValueError:
            print(msg)


def valideaza_interval(inceput, sfarsit):
    """
    Valideaza  un interval de timp astfel incat inceputul < sfarsit
    :param inceput: date time object
    :param sfarsit: date time object
    :return:
    """
    if inceput > sfarsit:
        raise Exception("Inceputul intervalului trebuie sa fie anterior sfarsitului acestuias")


def partitie(pachete, st, dr):
    """
    Partitie pentru quicks ort
    :param pachete: lista pachete
    :param st:marginea stanga pachet
    :param dr:marginea dreapta
    :return:
    """

    pivot = get_pret(pachete[dr])
    index_cur = st
    for i in range(st, dr):
        if pivot > get_pret(pachete[i]):
            a = pachete[index_cur]
            pachete[index_cur] = pachete[i]
            pachete[i] = a
            index_cur += 1
    a = pachete[index_cur]
    pachete[index_cur] = pachete[dr]
    pachete[dr] = a
    return index_cur


def quick_sort_pret(pachete, st, dr):
    """
    Functie sortare
    :param pachete: lista pachete
    :param st: margine stanga
    :param dr: margine dreapta
    :return:
    """
    if st < dr:
        pindex = partitie(pachete, st, dr)
        quick_sort_pret(pachete, st, pindex - 1)
        quick_sort_pret(pachete, pindex + 1, dr)

def afisare_calatorii(pachete):
    """
    Functie de afișare a pachetelor dintr-o lista sau a inexistenței lor în cazul în care nu există
    :param pachete: lista pachete
    :return:
    """
    print("AFIȘARE PACHETE CĂLĂTORII:")
    if type(pachete) is list:
        for i in range(len(pachete)):
            pachet = pachete[i]
            id = get_id(pachet)
            sosire = datetime.datetime.strftime(get_data_sosire(pachet), "%d.%m.%Y")
            plecare = datetime.datetime.strftime(get_data_plecare(pachet), "%d.%m.%Y")
            locatie = get_locatie(pachet).capitalize()
            pret = get_pret(pachet)
            print(f"{id}. Perioada de la: {sosire} pana la: {plecare} cu destinația {locatie} în Valoare de {pret} RON")
    else:
        print("Nu există Pachete de afișat ")


def add_to_undo(pachete, undo_list):
    if undo_list is not None:
        undo_list.append(pachete[:])
