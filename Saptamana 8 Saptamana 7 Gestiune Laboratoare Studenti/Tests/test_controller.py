import datetime

from Controller.crud import modify_student, add_student, delete_student, add_lab, delete_lab, modify_lab
from Domain.Student import Student


def test_add_student():
    studenti = []
    add_student(studenti, 'nume', 1)
    assert(studenti[0].nume == 'nume')
    assert(studenti[0].grupa == 1)
    try:
        add_student(studenti, '', -2)
        assert False
    except ValueError as ve:
        assert str(ve) == "Numele nu poate fi vid!\nGrupa nu poate fi negativa!\n"

def test_modify_student():
    studenti = []
    add_student(studenti, 'nume', 1)
    assert modify_student(studenti, 1, "new_nume", 2) == True
    assert(studenti[0].nume == 'new_nume')
    assert(studenti[0].grupa == 2)

    assert modify_student(studenti, 1, 'new_nume', -2) == False
    assert modify_student(studenti, 2, 'new_nume', 2) == False

    assert modify_student(studenti, 1, 'new_nume', 2) == True

def test_delete_student():
    studenti = []
    student = add_student(studenti, 'nume', 1)
    assert(delete_student(studenti, 1) == True)
    assert(delete_student(studenti,1) == False)


def test_add_lab():
    laboratoare = []
    deadline = datetime.datetime.strptime("25 10 2023", '%d %m %Y')
    assert add_lab(laboratoare, 1, 'descriere', deadline )
    assert not add_lab(laboratoare, 1, 'descriere', deadline )


def test_modify_lab():
    laboratoare = []
    deadline = datetime.datetime.strptime("25 10 2023", '%d %m %Y')
    deadline_2 = datetime.datetime.strptime("27 10 2023", '%d %m %Y')
    deadline_3 = datetime.datetime.strptime("27 10 2022", '%d %m %Y')
    laborator = add_lab(laboratoare, 1, 'descriere', deadline )
    assert modify_lab(laboratoare, 1, 'new_descriere', deadline_2)
    assert not modify_lab(laboratoare, 1, 'new_descriere', deadline_3)


def test_delete_lab():
    laboratoare = []
    deadline = datetime.datetime.strptime("25 10 2023", '%d %m %Y')
    laborator = add_lab(laboratoare, 1, 'descriere', deadline )
    assert(delete_lab(laboratoare, 1) == True)
    assert(delete_lab(laboratoare, 1) == False)


def test_controllers():
    test_add_student()
    test_modify_student()
    test_delete_student()
    test_add_lab()
    test_delete_lab()
    test_modify_lab()