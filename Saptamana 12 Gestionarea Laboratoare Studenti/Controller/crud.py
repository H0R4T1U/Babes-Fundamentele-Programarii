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
    try:
        id = studenti.get_all()[-1].id + 1
    except IndexError:
        id = 1

    student = Student(id, nume, grupa)
    try:
        valideaza_student(student, studenti.get_all())
    except ValueError as ve:
        raise ValueError(str(ve) + "Studentul nu a fost adăugat!\n")
    else:
        studenti.add(student)


def delete_student(studenti, id):
    """
    Functia sterge studentul cu id-ul dat
    :param studenti:
    :param id:
    :return:
    """
    return studenti.delete(id)


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
        raise Exception(str(ex) + "Studentul nu a fost modificat\n")
    else:
        if nume_nou == "":
            nume_nou = student.nume
        if grupa_noua == "":
            grupa_noua = student.grupa

        student_nou = Student(id, nume_nou, grupa_noua)
        try:
            valideaza_student(student_nou, studenti.get_all())
        except ValueError as ve:
            if str(ve) == "Id-ul exista deja!\n":
                studenti.update(student_nou)
            else:
                raise ValueError(str(ve) + "Studentul nu a fost modificat!\n")


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
        validate_lab(lab, laboratoare.get_all())
    except ValueError as ve:
        raise ValueError(str(ve) + "Laboratorul nu a fost Adăugat!\n")
    else:
        laboratoare.add(lab)


def delete_lab(laboratoare, id):
    """
    Functia sterge un laborator din lista de laboratoare
    :param laboratoare:
    :param id:
    :return:
    """
    return laboratoare.delete(id)


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
            validate_lab(lab_nou, laboratoare.get_all())
        except ValueError as ve:
            if str(ve) == "Laboratorul exista deja!\n":
                laboratoare.update(lab_nou)
            else:
                raise ValueError(str(ve) + "Laboratorul nu a fost modificat!\n")


def get_student_by_id(studenti, id):
    stud = studenti.get_by_id(id)
    if stud != -1:
        return stud
    else:
        raise Exception("Nu exista student cu id-ul dat!\n")


def get_lab_by_id(laboratoare, id):
    """
    Functia returneaza laboratorul cu id-ul dat
    :param laboratoare:
    :param id:
    :return:
    """
    lab = laboratoare.get_by_id(id)
    if lab != -1:
        return lab
    else:
        raise Exception("Nu exista nici un student cu id-ul dat!\n")


def get_student_by_name(studenti, nume_student):
    for student in studenti.get_all():
        if student.nume == nume_student:
            return student
    raise Exception("Nu exista nici un student cu numele dat!\n")
