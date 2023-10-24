from Repositories.pachetCRUD import get_id
def Validator(pachet,pachete):
    """
    Validează pachetul creat, si il adauga daca este ok
    :param pachet: Pachetul ce urmează adaugat
    :param pachete: lista de pachete
    :return: true sau Exceptie
    """
    id = get_id(pachet)
    msg = ""
    for p in pachete:
        if get_id(p) == id:
            msg +="ID-ul există deja \n"
    if msg != "":
        raise Exception(msg)
    else:
        return True