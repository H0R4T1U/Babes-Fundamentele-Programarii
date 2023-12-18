import unittest

from datetime import datetime

from Domain.Student import Student
from Domain.student_validator import valideaza_student
from Domain.lab_validator import validate_lab
from Domain.Laborator import Laborator
from Repository.LabRepository import LabRepository
from Repository.StudentiRepository import StudentRepository


class ValidatorTest(unittest.TestCase):
    def setUp(self):
        self.studenti = StudentRepository("Data/test_studenti.txt")
        self.laboratoare = LabRepository("Data/test_laboratoare.txt")

    def test_student_validator(self):
        student = Student(1, 'nume', 1)
        assert (valideaza_student(student,  self.studenti.get_all()) == True)
        self.studenti.add(student)
        try:
            valideaza_student(student,  self.studenti.get_all())
            assert False
        except ValueError as ve:
            assert str(ve) == "Id-ul exista deja!\n"

        student = Student(1, '', -15)
        try:
            valideaza_student(student,  self.studenti.get_all())
            assert False
        except ValueError as ve:
            assert str(ve) == "Id-ul exista deja!\nNumele nu poate fi vid!\nGrupa nu poate fi negativa!\n"


    def test_lab_validator(self):
        deadline = datetime.strptime("10 10 2023", "%d %m %Y")
        lab = Laborator(1, "descriere", deadline)
        assert validate_lab(lab, self.laboratoare.get_all())
        self.laboratoare.add(lab)
        try:
            validate_lab(lab, self.laboratoare.get_all())
            assert False
        except ValueError as ve:
            assert str(ve) == "Laboratorul exista deja!\n"
        lab = Laborator(-1, "descriere", deadline)
        try:
            validate_lab(lab, self.laboratoare.get_all())
            assert False
        except ValueError as ve:
            assert str(ve) == "Numarul laboratorului nu poate fi negativ!\n"
        lab = Laborator(1, "", deadline)
        try:
            validate_lab(lab, self.laboratoare.get_all())
            assert False
        except ValueError as ve:
            assert str(ve) == "Laboratorul exista deja!\nDescrierea nu poate fi vida!\n"
        lab = Laborator(1, "descriere", datetime.strptime("10 10 2022", "%d %m %Y"))
        try:
            validate_lab(lab, self.laboratoare.get_all())
            assert False
        except ValueError as ve:
            assert str(ve) == "Laboratorul exista deja!\nDeadline Invalid\n"
