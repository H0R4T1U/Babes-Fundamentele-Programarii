def create_student(id, nume, grupa):
    return {'id': id, 'nume': nume, 'grupa': grupa, 'laboratoare': [], 'note': [] }


def get_id(student):
    """
    Functia returneaza id-ul studentului
    :param student:
    :return:
    """
    return student['id']


def get_nume(student):
    """
    Functia returneaza numele studentului
    :param student:
    :return:
    """
    return student['nume']


def get_grupa(student):
    """
    Functia returneaza grupa studentului
    :param student:
    :return:
    """
    return student['grupa']


def get_laboratoare(student):
    """
    Functia returneaza lista de laboratoare la care este inscris studentul
    :param student:
    :return:
    """
    return student['laboratoare']


def get_note(student):
    """
    Functia returneaza lista de note a studentului
    :param student:
    :return:
    """
    return student['note']

# setters for all parmas
def set_id(student, id):
    """
    Functia seteaza id-ul studentului
    :param student:
    :param id:
    :return:
    """
    student['id'] = id


def set_nume(student, nume):
    """
    Functia seteaza numele studentului
    :param student:
    :param nume:
    :return:
    """
    student['nume'] = nume


def set_grupa(student, grupa):
    """
    Functia seteaza grupa studentului
    :param student:
    :param grupa:
    :return:
    """
    student['grupa'] = grupa


def set_laboratoare(student, laboratoare):
    """
    Functia seteaza lista de laboratoare la care este inscris studentul
    :param student:
    :param laboratoare:
    :return:
    """
    student['laboratoare'] = laboratoare


def set_note(student, note):
    """
    Functia seteaza lista de note a studentului
    :param student:
    :param note:
    :return:
    """
    student['note'] = note


def delete_student_id(studenti, id):
    """
    Functia sterge studentul cu id-ul dat
    :param studenti:
    :param id:
    :return:
    """
    for i in range(len(studenti)):
        if get_id(studenti[i]) == id:
            del studenti[i]
            return True
    return False


def get_student_by_id(studenti, id):
    for student in studenti:
        if get_id(student) == id:
            return student

    raise Exception("Nu exista student cu id-ul dat!")