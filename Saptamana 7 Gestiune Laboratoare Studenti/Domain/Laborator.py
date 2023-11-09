def create_lab(nr_lab, descriere, deadline):
    '''
    Functia creeaza un laborator
    :param nr_lab: numarul laboratorului
    :param descriere: descrierea laboratorului
    :param deadline: deadline-ul laboratorului
    :return: un dictionar cu atributele laboratorului
    '''
    return {
        'nr_lab':nr_lab,
        'descriere':descriere,
        'deadline':deadline
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
