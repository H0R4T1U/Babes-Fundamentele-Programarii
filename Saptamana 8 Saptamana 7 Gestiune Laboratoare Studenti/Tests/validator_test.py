from datetime import datetime

from Domain.Student import Student
from Domain.student_validator import valideaza_student
from Domain.lab_validator import validate_lab
from Domain.Laborator import  create_lab

def test_student_validator():
    studenti = []
    student = Student(1, 'nume', 1)
    assert(valideaza_student(student, studenti) == True)
    studenti.append(student)
    try:
        valideaza_student(student, studenti)
        assert False
    except ValueError as ve:
        assert str(ve) == "Id-ul exista deja!\n"

    student = Student(1, '', -15)
    try:
        valideaza_student(student,studenti)
        assert False
    except ValueError as ve:
        assert str(ve) == "Id-ul exista deja!\nNumele nu poate fi vid!\nGrupa nu poate fi negativa!\n"


def test_lab_validator():
    deadline = datetime.strptime("10 10 2023", "%d %m %Y")
    laboratoare = []
    lab = create_lab(1, "descriere", deadline)
    assert validate_lab(lab, laboratoare)
    laboratoare.append(lab)
    try:
        validate_lab(lab, laboratoare)
        assert False
    except ValueError as ve:
        assert str(ve) == "Laboratorul exista deja!\n"
    lab = create_lab(-1, "descriere", deadline)
    try:
        validate_lab(lab, laboratoare)
        assert False
    except ValueError as ve:
        assert str(ve) == "Numarul laboratorului nu poate fi negativ!\n"
    lab = create_lab(1, "", deadline)
    try:
        validate_lab(lab, laboratoare)
        assert False
    except ValueError as ve:
        assert str(ve) == "Laboratorul exista deja!\nDescrierea nu poate fi vida!\n"
    lab = create_lab(1, "descriere", datetime.strptime("10 10 2022", "%d %m %Y"))
    try:
        validate_lab(lab, laboratoare)
        assert False
    except ValueError as ve:
        assert str(ve) == "Laboratorul exista deja!\nDeadline Invalid\n"

def test_validators():
    test_lab_validator()
    test_student_validator()