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
    pass