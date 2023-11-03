import datetime

from Service.Services import cautare_pachete_interval, cautare_pachete_dest_pret, cautare_pachete_sfarsit, \
    raport_oferte_destinatie, raport_medie_pret_dest, raport_oferte_interval_cresc, filtrare_pret_destinatie, \
    filtrare_luna
from Service.crud import adauga_pachet_lista, get_pachet_by_id, SERVICE_modifica_pachet, \
    stergere_pachete_destinatie, stergere_pachete_data, stergere_pachete_pret
from Repositories.pachetCRUD import get_id,get_pret,get_locatie,get_data_plecare,get_data_sosire

def test_adauga_pachet_lista():
    pachete = []
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    locatie = "beius"
    pret = 1500
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    assert (len(pachete) == 1)
    try:
        data_plecare = datetime.datetime.strptime("25 03 2023", "%d %m %Y")
        adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
        assert False
    except Exception:
        assert True


def test_get_pachet():
    pachete = []
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    locatie = "beius"
    pret = 1500
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    assert (get_pachet_by_id(pachete, 1) == pachete[0])
    try:
        get_pachet_by_id(pachete, 5)
        assert False
    except Exception:
        assert True


def test_modifica_pachet():
    pachete = []
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    locatie = "beius"
    pret = 1500
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    SERVICE_modifica_pachet(pachete, 1, data_sosire, data_plecare, "oradea", pret)
    assert (get_locatie(pachete[0]) == 'oradea')
    try:
        SERVICE_modifica_pachet(pachete, 5, data_sosire, data_plecare, locatie, pret)
        assert False
    except Exception:
        assert True


def test_sterge_pachet_destinatie():
    pachete = []
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    locatie = "beius"
    pret = 1500

    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)

    adauga_pachet_lista(pachete, data_sosire, data_plecare, 'oradea', pret)
    assert (len(pachete) == 4)
    stergere_pachete_destinatie(pachete, "beius")
    assert (len(pachete) == 1)
    assert get_locatie(pachete[0]) == 'oradea'


def test_sterge_pachet_zile():
    pachete = []
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    locatie = "beius"
    pret = 1500
    data_plecare2 = datetime.datetime.strptime("25 09 2023", "%d %m %Y")

    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    adauga_pachet_lista(pachete, data_sosire, data_plecare2, locatie, pret)
    assert (len(pachete) == 3)
    stergere_pachete_data(pachete, 60)
    assert (len(pachete) == 1)
    assert get_data_plecare(pachete[0]) == data_plecare2


def test_sterge_pachet_pret():
    pachete = []
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    locatie = "beius"
    pret = 1500

    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, 999)
    assert (len(pachete) == 4)
    stergere_pachete_pret(pachete, 1000)
    assert (len(pachete) == 1)
    assert get_pret(pachete[0]) == 999


def test_cautare_interval():
    pachete = []
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    locatie = "beius"
    pret = 1500

    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 08 2023", "%d %m %Y")
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)

    cautare = cautare_pachete_interval(pachete, data_sosire, data_plecare)
    assert (len(cautare) == 1)
    assert get_id(cautare[0]) == 2
    assert get_data_plecare(cautare[0]) == data_plecare


def test_cautare_dest_pret():
    pachete = []
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    locatie = "beius"
    pret = 1500
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    locatie1 = "oradea"
    pret1 = 500
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie1, pret1)

    cautare = cautare_pachete_dest_pret(pachete, 'beius', 2000)
    assert len(cautare) == 1
    assert get_id(cautare[0]) == 1
    assert get_locatie(cautare[0]) == 'beius'

def test_cautare_sfarsit():

    pachete = []
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    locatie = "beius"
    pret = 1500
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 07 2023", "%d %m %Y")
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    cautare = cautare_pachete_sfarsit(pachete, data_plecare)
    assert len(cautare) == 1
    assert get_id(cautare[0]) == 2
    assert get_data_plecare(cautare[0]) == data_plecare


def test_raport_destinatie():
    pachete = []
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    locatie = "beius"
    pret = 1500
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)

    adauga_pachet_lista(pachete, data_sosire, data_plecare, 'oradea', pret)

    assert (raport_oferte_destinatie(pachete, 'beius') == [pachete[0]])


def test_raport_intreval_cresc():
    pachete = []
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    data_plecare2 = datetime.datetime.strptime("29 04 2023", "%d %m %Y")
    locatie = "beius"
    pret = 1500
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    adauga_pachet_lista(pachete, data_sosire, data_plecare2, locatie, 2500)
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, 1000)

    pachete_interval = raport_oferte_interval_cresc(pachete, data_sosire, data_plecare)
    assert len(pachete_interval) == 2
    assert get_id(pachete_interval[0]) == 3
    assert get_id(pachete_interval[1]) == 1

def test_raport_sum_dest():
    pachete = []
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    locatie = "beius"
    pret = 1500
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, 2500)

    assert raport_medie_pret_dest(pachete, 'beius') == 2000


def test_filtrare_pret_destinatie():
    pachete = []
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    locatie = "beius"
    pret = 1500
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    locatie1 = "oradea"
    pret1 = 2000
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie1, pret1)

    assert len(pachete) == 2
    assert filtrare_pret_destinatie(pachete, 'beius', 1500) == 1
    assert len(pachete) == 1
    assert get_locatie(pachete[0]) == 'beius'

def test_filtrare_luna():
    pachete = []
    data_sosire = datetime.datetime.strptime("25 01 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 07 2023", "%d %m %Y")
    locatie = "beius"
    pret = 1500
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)

    data_sosire1 = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    data_plecare1 = datetime.datetime.strptime("25 02 2024", "%d %m %Y")
    adauga_pachet_lista(pachete, data_sosire1, data_plecare1, locatie, pret)

    data_sosire2 = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare2 = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    adauga_pachet_lista(pachete, data_sosire2, data_plecare2, locatie, pret)
    assert len(pachete) == 3
    assert filtrare_luna(pachete, 1) == 2
    assert len(pachete) == 1
    assert get_id(pachete[0]) == 3


def test_all_services():
    test_adauga_pachet_lista()
    test_get_pachet()
    test_modifica_pachet()
    test_sterge_pachet_destinatie()
    test_sterge_pachet_zile()
    test_sterge_pachet_pret()
    test_cautare_interval()
    test_cautare_dest_pret()
    test_cautare_sfarsit()
    test_raport_destinatie()
    test_raport_intreval_cresc()
    test_raport_sum_dest()
    test_filtrare_pret_destinatie()
    test_filtrare_luna()