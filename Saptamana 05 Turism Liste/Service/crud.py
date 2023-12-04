from Repositories.Validator import Validator
from Repositories.pachetCRUD import *


def adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret):
    """
    Adauga un pachet in lista de pachete
    :param pachete: lista de pachete
    :param data_sosire: data de sosire a pachetului
    :param data_plecare: data de plecare a pachetului
    :param locatie: locatia pachetului
    :param pret: pretul pachetului
    :return:
    """

    length = len(pachete)
    if length > 0:
        id = get_id(pachete[length-1]) + 1
    else:
        id = 1

    pachet = creaza_pachet(id, data_sosire, data_plecare, locatie, pret)
    try:
        Validator(pachet, pachete)
    except Exception as ex:
        print(ex)
    else:
        pachete.append(pachet)


def get_pachet_by_id(pachete, id):
    """
    Obtine un pachet din lista cu id-ul specificat
    :param pachete: lista pachete
    :param id: id-ul pachetului
    :return: Pachetul cu id-ul id
    """
    if id > len(pachete):
        raise Exception("ID-ul nu există!")
    else:
        for i in pachete:
            if get_id(i) == id:
                return i


def SERVICE_modifica_pachet(pachete, id, data_sosire, data_plecare, locatie, pret):
    """
    Modifică un pachet existent
    :param pachete: lista pachete
    :param id: id pachet
    :param data_sosire:data sosire noua
    :param data_plecare: data plecare noua
    :param locatie: locatia noua
    :param pret: pret nou
    :return: -
    """
    try:
        pachet = get_pachet_by_id(pachete, id)
    except Exception as ex:
        print(ex)
    else:
        pachet_nou = modifica_pachet(pachet, data_sosire, data_plecare, locatie, pret)
        try:
            Validator(pachete, pachet_nou)
        except Exception as ex:
            if ex == "ID-ul există deja \n":
                for i in range(len(pachete)):
                    if get_id(pachete[i]) == get_id(pachet_nou):
                        pachete[i] = pachet_nou


def stergere_pachete_destinatie(pachete, destinatie):
    """
    Sterge toate pachetele dintr-o destinatie
    :param pachete: lista pachete
    :param destinatie: destinatia de sters
    :return:
    """
    length = len(pachete)
    i = 0
    while i < length:
        if get_locatie(pachete[i]) == destinatie:
            sterge_pachet(pachete, get_id(pachete[i]))
            i -= 1
            length -= 1
        i += 1


def stergere_pachete_data(pachete, zile):
    """
    Sterge toate pachetele cu o durata mai scurta decat nr de zile precizat
    :param pachete: lista pachete
    :param zile: nr de zile
    :return:
    """
    length = len(pachete)
    i = 0
    while i < length:
        time_delta = get_data_plecare(pachete[i]) - get_data_sosire(pachete[i])
        if time_delta.days < zile:
            sterge_pachet(pachete, get_id(pachete[i]))
            i -= 1
            length -= 1
        i += 1


def stergere_pachete_pret(pachete, pret):
    """
    Sterge pachetelor cu pretul mai mare decat cel dat
    :param pachete: lista pachete
    :param pret: suma
    :return:
    """
    length = len(pachete)
    i = 0
    while i < length:
        if get_pret(pachete[i]) > pret:
            sterge_pachet(pachete, get_id(pachete[i]))
            i -= 1
            length -= 1
        i += 1
