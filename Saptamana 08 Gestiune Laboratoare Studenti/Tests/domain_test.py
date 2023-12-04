import datetime

from Domain.Laborator import Laborator
from Domain.Student import Student


def test_creaza_lab():
    """
    Functia testeaza creeaza_lab
    :return:
    """
    lab = Laborator(1, 'descriere', 'deadline')
    assert (lab.id == 1)
    assert (lab.descriere == 'descriere')
    assert (lab.deadline == 'deadline')


def test_lab_seters():
    """
    Functia testeaza set_deadline si set_descriere
    :return:
    """
    lab = Laborator(1, 'descriere', 'deadline')
    lab.deadline = 'new_deadline'
    lab.descriere = 'new_descriere'
    lab.id = 2
    assert (lab.deadline == 'new_deadline')
    assert (lab.descriere == 'new_descriere')
    assert (lab.id == 2)


def test_create_student():
    """
    Functia testeaza creeaza_student
    :return:
    """
    student = Student(1, 'nume', 1)
    assert (student.id == 1)
    assert (student.nume == 'nume')
    assert (student.grupa == 1)
    assert (student.laboratoare == [])
    assert (student.note == [])


def test_student_seters():
    """
    Functia testeaza set_id, set_nume, set_grupa
    :return:
    """
    student = Student(1, 'nume', 1)
    student.id = 2
    student.nume = "new_nume"
    student.grupa = 3

    assert (student.id == 2)
    assert (student.nume == 'new_nume')
    assert (student.grupa == 3)


def test_all_domain():
    """
    Functia testeaza toate functiile din domeniu
    :return:
    """
    test_creaza_lab()
    test_lab_seters()
    test_create_student()
    test_student_seters()