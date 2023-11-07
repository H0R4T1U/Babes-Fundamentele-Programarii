import datetime

from Repositories.pachetCRUD import sterge_pachet, get_id
from Service.Services import filtrare_luna, undo
from Service.crud import adauga_pachet_lista
from Utility.utility import afisare_calatorii, add_to_undo


def batch_add(pachete, undo_list, data_sosire, data_plecare, locatie, pret):
    data_sosire = datetime.datetime.strptime(data_sosire, "%d.%m.%Y")
    data_plecare = datetime.datetime.strptime(data_plecare, "%d.%m.%Y")

    adauga_pachet_lista(pachete, data_sosire, data_plecare, locatie, pret,undo_list )


def batch_delete(pachete, undo_list, id=None):
    """
    Sterge pachete
    :param pachete: lista pachete
    :param undo_list: lista undo
    :return:
    """
    add_to_undo(pachete, undo_list)
    if id != 0:
        sterge_pachet(pachete, id)
    else:
        for pachet in pachete:
            id = get_id(pachet)
            sterge_pachet(pachete, id)


def batch_filter(pachete, undo_list):
    """
    Filter
    :param pachete: lista pachete
    :param undo_list: lista operatiuni anterioare
    :return:
    """
    filtrare_luna(pachete, 4, undo_list)


def batch_undo(pachete, undo_list):
    """
    Undo pachete
    :param pachete: Lista pachete
    :param undo_list: lista operatiuni anterioare
    :return:
    """

    return undo(pachete, undo_list)

def batch_mode(pachete, undo_list):
    """

    :param pachete: lista pachete
    :param undo_list: lista operatiuni anterioare
    :return:
    """
    print("Introduceți comenzile(SEPARATE DE ;):")
    cmd = input(":").lower()
    comenzi = cmd.split(";")
    for i in range(len(comenzi)):
        c = comenzi[i].split(" ")
        comanda = c[0]
        try:
            nr = int(c[1])
        except IndexError:
            comanda = c[0]
            nr = 0

        except ValueError:
            comanda = c[0]
            nr = 0
        finally:
            if comanda == "add":
                data = c[1]
                data = data.split("/")
                data_sosire = data[0]
                data_plecare = data[1]
                locatie = c[2]
                pret = c[3]
                batch_add(pachete, undo_list, data_sosire,data_plecare,locatie,pret)
                print("Adaugare:")
                afisare_calatorii(pachete)
                print("\n")
            if comanda == "delete":
                batch_delete(pachete, undo_list, nr)
                print("Delete:")
                afisare_calatorii(pachete)
                print("\n")
            if comanda == "filter":
                batch_filter(pachete, undo_list)
                print("Filter:")
                afisare_calatorii(pachete)
                print("\n")
            if comanda == "undo":
                pachete = batch_undo(pachete, undo_list)
                print("Undo:")
                afisare_calatorii(pachete)
                print("\n")
