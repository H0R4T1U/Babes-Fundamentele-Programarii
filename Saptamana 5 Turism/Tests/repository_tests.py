import datetime

from Repositories.pachetCRUD import *
from Repositories.Validator import Validator

def test_add_pachet():
    id = 1
    data_sosire = datetime.datetime.strptime("15 10 2022", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("16 10 2022", "%d %m %Y")
    locatie = 'beius'
    pret = 2500
    pachet = creaza_pachet(id, data_sosire, data_plecare, locatie, pret)
    assert(get_id(pachet) == id)
    assert( get_data_sosire(pachet) == data_sosire)
    assert (get_data_plecare(pachet) == data_plecare)
    assert (get_pret(pachet) == pret)


def test_validare_pachet():
    pachete = []
    id = 1
    data_sosire = datetime.datetime.strptime("15 10 2022", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("16 10 2022", "%d %m %Y")
    locatie = 'beius'
    pret = 2500
    pachet = creaza_pachet(id, data_sosire, data_plecare, locatie, pret)
    assert(Validator(pachet,[]) == True)
    pachete.append(pachet)
    try:
        Validator(pachet,pachete)
        assert(False)
    except Exception:
        assert(True)


def test_modifica_pachet():
    id = 1
    data_sosire = datetime.datetime.strptime("15 10 2022", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("16 10 2022", "%d %m %Y")
    locatie = 'beius'
    pret = 2500
    pachet = creaza_pachet(id, data_sosire, data_plecare, locatie, pret)
    pachet = modifica_pachet(pachet,data_sosire,data_plecare,'oradea',3100)

    assert(get_pret(pachet) == 3100 )
    assert(get_locatie(pachet) == 'oradea')


def test_sterge_pachet():
    pachete = []
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    locatie = "beius"
    pret = 1500
    pachete.append(creaza_pachet(1, data_sosire, data_plecare, locatie, pret))

    pachete.append(creaza_pachet(2, data_sosire, data_plecare, locatie, pret))
    pachete.append(creaza_pachet(3, data_sosire, data_plecare, locatie, pret))
    sterge_pachet(pachete,2)
    assert(len(pachete) == 2)



def test_all_repositories():
    test_add_pachet()
    test_validare_pachet()
    test_modifica_pachet()
    test_sterge_pachet()