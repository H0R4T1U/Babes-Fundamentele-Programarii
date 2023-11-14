def create_lab(nr_lab, descriere, deadline):
    '''
    Functia creeaza un laborator
    :param nr_lab: numarul laboratorului
    :param descriere: descrierea laboratorului
    :param deadline: deadline-ul laboratorului
    :return: un dictionar cu atributele laboratorului
    '''
    return {
        'nr_lab': nr_lab,
        'descriere': descriere,
        'deadline': deadline
    }


def get_nr_lab(lab):
    '''
    Functia returneaza numarul laboratorului
    :param lab: laboratorul
    :return: numarul laboratorului
    '''
    return lab['nr_lab']


def get_descriere(lab):
    '''
    Functia returneaza descrierea laboratorului
    :param lab: laboratorul
    :return: descrierea laboratorului
    '''
    return lab['descriere']


def get_deadline(lab):
    '''
    Functia returneaza deadline-ul laboratorului
    :param lab: laboratorul
    :return: deadline-ul laboratorului
    '''
    return lab['deadline']


def set_deadline(lab, deadline):
    '''
    Functia seteaza deadline-ul laboratorului
    :param lab: laboratorul
    :param deadline: deadline-ul laboratorului
    :return: -
    '''
    lab['deadline'] = deadline


def set_descriere(lab, descriere):
    '''
    Functia seteaza descrierea laboratorului
    :param lab: laboratorul
    :param descriere: descrierea laboratorului
    :return: -
    '''
    lab['descriere'] = descriere


def set_nr_lab(lab, nr_lab):
    '''
    Functia seteaza numarul laboratorului
    :param lab: laboratorul
    :param nr_lab: numarul laboratorului
    :return: -
    '''
    lab['nr_lab'] = nr_lab


def delete_lab_id(laboratoare, id):
    '''
    Functia sterge un laborator din lista de laboratoare
    :param laboratoare: lista de laboratoare
    :param id: id-ul laboratorului de sters
    :return: -
    '''
    to_delete = []
    for i in range(len(laboratoare)):
        if get_nr_lab(laboratoare[i]) == id:
            del laboratoare[i]
            return True
    return False

def get_lab_by_id(laboratoare,id):
    """
    Functia returneaza laboratorul cu id-ul dat
    :param laboratoare:
    :param id:
    :return:
    """
    for lab in laboratoare:
        if get_nr_lab(lab) == id:
            return lab
    raise Exception("Nu exista student cu id-ul dat!")