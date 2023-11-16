from Domain.Laborator import Laborator
from Domain.Student import Student
from Domain.lab_validator import validate_lab
from Domain.student_validator import valideaza_student


def add_student(studenti, nume, grupa):
    """
    Functia adauga un student in lista de studenti
    :param studenti:lista studenti
    :param nume:nume student
    :param grupa:grupa student
    :return:Adauga student la lista sau Raise ValueError
    """
    id = len(studenti) + 1
    student = Student(id, nume, grupa)
    try:
        valideaza_student(student, studenti)
    except ValueError as ve:
        raise ValueError(str(ve)+"Studentul nu a fost adăugat!\n")
    else:
        studenti.append(student)


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
    :param studenti:Lista studenti
    :param id: id student de modificat
    :param nume_nou: nume nou student
    :param grupa_noua: grupa noua student
    :return:Modifica studentul sau Raise Exception/Value Error
    """
    try:
        student = get_student_by_id(studenti, id)
    except Exception as ex:
        raise Exception(str(ex)+"Studentul nu a fost modificat\n")
    else:
        if nume_nou == "":
            nume_nou = student.nume
        if grupa_noua == "":
            grupa_noua = student.grupa

        student_nou = Student(id, nume_nou, grupa_noua)
        try:
            valideaza_student(student_nou, studenti)
        except ValueError as ve:
            if str(ve) == "Id-ul exista deja!\n":
                for i in range(len(studenti)):
                    if studenti[i].id == id:
                        studenti[i] = student_nou
                        return True
            else:
                raise ValueError(str(ve)+"Studentul nu a fost modificat!\n")


def add_lab(laboratoare, nr_lab, descriere, deadline):
    """
    Functia adauga un laborator in lista de laboratoare
    :param laboratoare:Lista laboratoare
    :param nr_lab:lab de adăugat
    :param descriere:Descriere Lab
    :param deadline:deadline laborator
    :return:Adauga laborator la lista sau ValueError
    """
    lab = Laborator(nr_lab, descriere, deadline)
    try:
       validate_lab(lab, laboratoare)
    except ValueError as ve:
        raise ValueError(str(ve)+"Laboratorul nu a fost Adăugat!\n")
    else:
        laboratoare.append(lab)

def delete_lab(laboratoare, id):
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
        raise Exception(str(ex) + "Laboratorul nu a fost modificat!\n")
    else:
        if descriere_noua == "":
            descriere_noua = lab.descriere
        if deadline_nou == "":
            deadline_nou = lab.deadline

        lab_nou = Laborator(id, descriere_noua, deadline_nou)
        try:
            validate_lab(lab_nou, laboratoare)
        except ValueError as ve:
            if str(ve) == "Laboratorul exista deja!\n":
                for i in range(len(laboratoare)):
                    if laboratoare[i].id == id:
                        laboratoare[i] = lab_nou
                        return True
            else:
                raise ValueError(str(ve)+"Laboratorul nu a fost modificat!\n")

def delete_student_id(studenti, id):
    """
    Functia sterge studentul cu id-ul dat
    :param studenti:
    :param id:
    :return:
    """
    for i in range(len(studenti)):
        if studenti[i].id == id:
            del studenti[i]
            return True
    return False


def get_student_by_id(studenti, id):
    for student in studenti:
        if student.id == id:
            return student

    raise Exception("Nu exista student cu id-ul dat!\n")


def delete_lab_id(laboratoare, id):
    '''
    Functia sterge un laborator din lista de laboratoare
    :param laboratoare: lista de laboratoare
    :param id: id-ul laboratorului de sters
    :return: -
    '''
    to_delete = []
    for i in range(len(laboratoare)):
        if laboratoare[i].id == id:
            del laboratoare[i]
            return True
    return False


def get_lab_by_id(laboratoare, id):
    """
    Functia returneaza laboratorul cu id-ul dat
    :param laboratoare:
    :param id:
    :return:
    """
    for lab in laboratoare:
        if lab.id == id:
            return lab
    raise Exception("Nu exista nici un student cu id-ul dat!\n")


def get_student_by_name(studenti, nume_student):
    for student in studenti:
        if student.nume == nume_student:
            return student
    raise Exception("Nu exista nici un student cu numele dat!\n")
