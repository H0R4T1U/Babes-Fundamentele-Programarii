def creaza_pachet(id, data_sosire, data_plecare, locatie, pret):
    """
    Creaza un pachet cu inputul utilizatorului
    :param id: Id ul pachetului
    :param data_sosire: datetime object semnificand data de sosire
    :param data_plecare: datetime object semnificand data de plecare
    :param locatie: string semnificand locatia in care se va afla calatoria
    :param pret: numar >0 care semnifica pretul calatoriei
    :return: pachetul cu inputurile sub forma de dictionar
    """
    return {'id': id,
            'data_sosire': data_sosire,
            'data_plecare': data_plecare,
            'locatie': locatie,
            'pret': pret
            }


def get_id(pachet):
    """
    returneaza id ul pachetului
    :param pachet:
    :return:
    """
    return pachet['id']


def get_data_sosire(pachet):
    """
    returneaza data de sosire a pachetului
    :param pachet:
    :return:
    """
    return pachet['data_sosire']


def get_data_plecare(pachet):
    """
    Returneaza data de plecare a pachetului
    :param pachet:
    :return:
    """
    return pachet['data_plecare']


def get_locatie(pachet):
    """
    returneaza locatia pachetului
    :param pachet:
    :return:
    """
    return pachet['locatie']


def get_pret(pachet):
    """
    returneaza pretul pachetului
    :param pachet:
    :return:
    """
    return pachet['pret']


def modifica_pachet(pachet, data_sosire, data_plecare, locatie, pret):
    """
    Modifica un pachet
    :param pachet:
    :param data_sosire:
    :param data_plecare:
    :param locatie:
    :param pret:
    :return:
    """

    pachet['data_sosire'] = data_sosire
    pachet['data_plecare'] = data_plecare
    pachet['locatie'] = locatie
    pachet['pret'] = pret
    return pachet


def sterge_pachet(pachete, id):
    to_delete = []
    for i in range(len(pachete)):
        if pachete[i]['id'] == id:
            to_delete.append(i)
    start = len(to_delete)
    for i in range(start):
        index = to_delete[i]
        del pachete[index - i]
