import datetime

from Repositories.pachetCRUD import get_id
from Service.crud import adauga_pachet_lista
from Utility.utility import quick_sort_pret


def test_quick_sort_pret():
    pachete = []
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    locatie = "beius"
    pret = 1500

    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    pret = 1000
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    pret = 1300
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)

    assert (get_id(pachete[0]) == 1)
    assert (get_id(pachete[1]) == 2)
    assert (get_id(pachete[2]) == 3)

    quick_sort_pret(pachete, 0, len(pachete)-1)

    assert(get_id(pachete[0]) == 2)
    assert(get_id(pachete[1]) == 3)
    assert(get_id(pachete[2]) == 1)


def test_all_utility():
    test_quick_sort_pret()
