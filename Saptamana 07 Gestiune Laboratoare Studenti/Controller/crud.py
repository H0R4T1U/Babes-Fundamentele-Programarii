from Domain.Laborator import create_lab, delete_lab_id, get_lab_by_id, get_descriere, get_deadline, get_nr_lab
from Domain.Student import create_student, get_id, delete_student_id, get_student_by_id, get_nume, get_grupa
from Domain.lab_validator import validate_lab
from Domain.student_validator import valideaza_student


def add_student(studenti, nume, grupa):
    """
    Functia adauga un student in lista de studenti
    :param studenti:
    :param nume:
    :param grupa:
    :return:
    """
    id = len(studenti) + 1
    student = create_student(id, nume, grupa)
    if valideaza_student(student, studenti):
        studenti.append(student)
        return True
    return False


def delete_student(studenti, id):
    """
    Functia sterge studentul cu id-ul dat
    :param studenti:
    :param id:
    :return:
    """
    return delete_student_id(studenti, id)


def modify_student(studenti, id, nume_nou, grupa_noua):
    """
    Functia modifica un student
    :param studenti:
    :param id:
    :param nume_nou:
    :param grupa_noua:
    :return:
    """
    try:
        student = get_student_by_id(studenti, id)
    except Exception as ex:
        print(ex)
        return False
    else:
        if nume_nou == "":
            nume_nou = get_nume(student)
        if grupa_noua == "":
            grupa_noua = get_grupa(student)

        student_nou = create_student(id, nume_nou, grupa_noua)
        try:
            valideaza_student(student_nou, studenti)
        except ValueError as ve:
            if str(ve) == "Id-ul exista deja!\n":
                for i in range(len(studenti)):
                    if get_id(studenti[i]) == id:
                        studenti[i] = student_nou
                        return True
            else:
                print(ve)
                return False



def add_lab(laboratoare, nr_lab, descriere, deadline):
    """
    Functia adauga un laborator in lista de laboratoare
    :param laboratoare:
    :param nr_lab:
    :param descriere:
    :param deadline:
    :return:
    """
    lab = create_lab(nr_lab, descriere, deadline)
    try:
        if validate_lab(lab, laboratoare):
            laboratoare.append(lab)
            return True
    except ValueError as ve:
        print(ve)
        return False

def delete_lab(laboratoare,id):
    """
    Functia sterge un laborator din lista de laboratoare
    :param laboratoare:
    :param id:
    :return:
    """
    return delete_lab_id(laboratoare, id)


def modify_lab(laboratoare, id, descriere_noua, deadline_nou):
    """
    Functia modifica un laborator
    :param laboratoare:
    :param id:
    :param descriere_noua:
    :param deadline_nou:
    :return:
    """
    try:
        lab = get_lab_by_id(laboratoare, id)
    except Exception as ex:
        print(ex)
        return False
    else:
        if descriere_noua == "":
            descriere_noua = get_descriere(lab)
        if deadline_nou == "":
            deadline_nou = get_deadline(lab)

        lab_nou = create_lab(id, descriere_noua, deadline_nou)
        try:
            validate_lab(lab_nou, laboratoare)
        except ValueError as ve:
            if str(ve) == "Laboratorul exista deja!\n":
                for i in range(len(laboratoare)):
                    if get_nr_lab(laboratoare[i]) == id:
                        laboratoare[i] = lab_nou
                        return True
            else:
                print(ve)
                return False