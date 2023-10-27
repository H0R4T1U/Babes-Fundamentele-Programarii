import datetime
import os

from Repositories.pachetCRUD import get_pret


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
