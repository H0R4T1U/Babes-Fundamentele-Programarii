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
        id = pachete[length-1]['id'] + 1
    else:
        id = 1

    pachet = creaza_pachet(id, data_sosire, data_plecare, locatie, pret)
    try:
        Validator(pachet, pachete)
    except Exception as ex:
        print(ex)
    else:
        pachete.append(pachet)


def get_pachet_by_id(pachete,id):
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
            if i['id'] == id:
                return i


def SERVICE_modifica_pachet(pachete, id, data_sosire, data_plecare, locatie, pret):
    try:
        pachet = get_pachet_by_id(pachete, id)
    except Exception as ex:
        print(ex)

    pachet_nou = modifica_pachet(pachet, data_sosire, data_plecare, locatie, pret)
    try:
        Validator(pachete,pachet_nou)
    except Exception as ex:
        if ex == "ID-ul există deja \n":
            for i in range(len(pachete)):
                if pachete[i]['id'] == pachet_nou['id']:
                    pachete[i] = pachet_nou


def stergere_pachete_destinatie(pachete, destinatie):
    length = len(pachete)
    i = 0
    while i < length:
        if get_locatie(pachete[i]) == destinatie:
            sterge_pachet(pachete, get_id(pachete[i]))
            i -= 1
            length -= 1
        i += 1


def stergere_pachete_data(pachete,zile):
    length = len(pachete)
    i = 0
    while i < length:
        time_delta = get_data_plecare(pachete[i]) - get_data_sosire(pachete[i])
        if time_delta.days < zile:
            sterge_pachet(pachete, get_id(pachete[i]))
            i -= 1
            length -= 1
        i += 1


def stergere_pachete_pret(pachete,pret):
    length = len(pachete)
    i = 0
    while i < length:
        if pachete[i]['pret'] > pret:
            sterge_pachet(pachete,pachete[i]['id'])
            i -= 1
            length -= 1
        i += 1