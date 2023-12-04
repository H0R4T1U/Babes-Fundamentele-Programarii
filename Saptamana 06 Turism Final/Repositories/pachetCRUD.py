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

    return [id, data_sosire, data_plecare, locatie, pret]


def get_id(pachet):
    """
    returneaza id ul pachetului
    :param pachet: pachetul
    :return: id-ul sau
    """
    return pachet[0]


def get_data_sosire(pachet):
    """
    returneaza data de sosire a pachetului
    :param pachet: pachetul
    :return: data de sosire
    """
    return pachet[1]


def get_data_plecare(pachet):
    """
    Returneaza data de plecare a pachetului
    :param pachet:pachetul
    :return:data de plecare
    """
    return pachet[2]


def get_locatie(pachet):
    """
    returneaza locatia pachetului
    :param pachet:pachetul
    :return:locatia
    """
    return pachet[3]


def get_pret(pachet):
    """
    returneaza pretul pachetului
    :param pachet:pachetul
    :return:pretul sau
    """
    return pachet[4]


def modifica_pachet(pachet, data_sosire, data_plecare, locatie, pret):
    """
    Modifica un pachet
    :param pachet:pachetul
    :param data_sosire:data de sosire noua
    :param data_plecare:data de plecare noua
    :param locatie:locatia noua
    :param pret:pretul nou
    :return:pachetul nou
    """

    pachet[1] = data_sosire
    pachet[2] = data_plecare
    pachet[3] = locatie
    pachet[4] = pret
    return pachet


def sterge_pachet(pachete, id):
    """
    Sterge un pachet din lista de pachete
    :param pachete: lista de pachete
    :param id: id-ul pachetului de sters
    :return:
    """
    to_delete = []
    for i in range(len(pachete)):
        if get_id(pachete[i]) == id:
            to_delete.append(i)
    start = len(to_delete)
    for i in range(start):
        index = to_delete[i]
        del pachete[index - i]
