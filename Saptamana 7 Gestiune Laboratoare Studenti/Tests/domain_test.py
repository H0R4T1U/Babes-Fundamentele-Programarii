import datetime

from Domain.Laborator import create_lab, get_nr_lab, get_descriere, get_deadline, set_deadline, set_descriere, \
    set_nr_lab, delete_lab_id
from Domain.Student import create_student, get_id, get_nume, get_grupa, get_laboratoare, get_note, set_id, set_nume, \
    set_grupa, delete_student_id


def test_creaza_lab():
    """
    Functia testeaza creeaza_lab
    :return:
    """
    lab = create_lab(1, 'descriere', 'deadline')
    assert (get_nr_lab(lab) == 1)
    assert (get_descriere(lab) == 'descriere')
    assert (get_deadline(lab) == 'deadline')


def test_lab_seters():
    """
    Functia testeaza set_deadline si set_descriere
    :return:
    """
    lab = create_lab(1, 'descriere', 'deadline')
    set_deadline(lab, 'new_deadline')
    set_descriere(lab, 'new_descriere')
    set_nr_lab(lab, 2)
    assert (get_deadline(lab) == 'new_deadline')
    assert (get_descriere(lab) == 'new_descriere')
    assert (get_nr_lab(lab) == 2)


def test_create_student():
    """
    Functia testeaza creeaza_student
    :return:
    """
    student = create_student(1, 'nume', 1)
    assert (get_id(student) == 1)
    assert (get_nume(student) == 'nume')
    assert (get_grupa(student) == 1)
    assert (get_laboratoare(student) == [])
    assert (get_note(student) == [])


def test_student_seters():
    """
    Functia testeaza set_id, set_nume, set_grupa
    :return:
    """
    student = create_student(1, 'nume', 1)
    set_id(student, 2)
    set_nume(student, 'new_nume')
    set_grupa(student, 3)
    assert (get_id(student) == 2)
    assert (get_nume(student) == 'new_nume')
    assert (get_grupa(student) == 3)


def test_delete_student_by_id():
    """
    Functia testeaza delete_student_by_id
    :return:
    """
    studenti = []
    student = create_student(1, 'nume', 1)
    studenti.append(student)
    assert (delete_student_id(studenti, 1) == True)
    delete_student_id(studenti, 1 == False)


def test_delete_lab_by_id():
    """
    Functia testeaza delete_lab_by_id
    :return:
    """
    laboratoare = []
    lab = create_lab(1, 'descriere', datetime.datetime.strptime("25 10 2023", '%d %m %Y'))
    laboratoare.append(lab)
    assert (delete_lab_id(laboratoare, 1) == True)
    assert (delete_lab_id(laboratoare, 1) == False)

def test_all_domain():
    """
    Functia testeaza toate functiile din domeniu
    :return:
    """
    test_creaza_lab()
    test_lab_seters()
    test_create_student()
    test_student_seters()
    test_delete_student_by_id()
    test_delete_lab_by_id()