import datetime
from Service.crud import adauga_pachet_lista, get_pachet_by_id, SERVICE_modifica_pachet, sterge_pachet, \
    stergere_pachete_destinatie, stergere_pachete_data, stergere_pachete_pret


def test_adauga_pachet_lista():
    pachete = []
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    locatie = "beius"
    pret = 1500
    adauga_pachet_lista(pachete,data_sosire,data_plecare,locatie,pret)
    assert(len(pachete) == 1 )
    try:
        data_plecare = datetime.datetime.strptime("25 03 2023", "%d %m %Y")
        adauga_pachet_lista(data_sosire,data_plecare,locatie,pret)
        assert(False)
    except Exception:
        assert(True)


def test_get_pachet():
    pachete = []
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    locatie = "beius"
    pret = 1500
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    assert(get_pachet_by_id(pachete, 1) == pachete[0])
    try:
        get_pachet_by_id(pachete,5)
        assert(False)
    except Exception:
        assert(True)


def test_modifica_pachet():
    pachete = []
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    locatie = "beius"
    pret = 1500
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    SERVICE_modifica_pachet(pachete,1,data_sosire,data_plecare,"oradea",pret)
    assert(pachete[0]['locatie'] == 'oradea')
    try:
        SERVICE_modifica_pachet(pachete,5,data_sosire,data_plecare,locatie,pret)
        assert(False)
    except Exception:
        assert(True)



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
    assert(len(pachete) == 1)


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
    stergere_pachete_data(pachete,60)
    assert(len(pachete) == 1)


def test_sterge_pachet_pret():
    pachete = []
    data_sosire = datetime.datetime.strptime("25 04 2023", "%d %m %Y")
    data_plecare = datetime.datetime.strptime("25 05 2023", "%d %m %Y")
    locatie = "beius"
    pret = 1500

    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret)
    adauga_pachet_lista(pachete,data_sosire,data_plecare,locatie,999)
    assert(len(pachete) == 4)
    stergere_pachete_pret(pachete,1000)
    assert(len(pachete) == 1)

def test_all_services():
    test_adauga_pachet_lista()
    test_get_pachet()
    test_modifica_pachet()
    test_sterge_pachet_destinatie()
    test_sterge_pachet_zile()
    test_sterge_pachet_pret()