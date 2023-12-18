import datetime
import unittest

from Controller.crud import modify_student, add_student, delete_student, add_lab, delete_lab, modify_lab
from Repository.LabRepository import LabRepository
from Repository.StudentiRepository import StudentRepository

class TestStudentController(unittest.TestCase):
    def setUp(self):
        self.studenti = StudentRepository("Data/test_studenti.txt")
        self.laboratoare = LabRepository("Data/test_Lab.txt")


    def test_add_student(self):
        add_student(self.studenti, 'nume', 1)
        assert (self.studenti.get_all()[0].nume == 'nume')
        assert (self.studenti.get_all()[0].grupa == 1)
        try:
            add_student(self.studenti, '', -2)
            assert False
        except ValueError as ve:
            assert True


    def test_modify_student(self):
        add_student(self.studenti, 'nume', 1)
        modify_student(self.studenti, 1, "new_nume", 2)
        assert (self.studenti.get_all()[0].nume == 'new_nume')
        assert (self.studenti.get_all()[0].grupa == 2)
        try:
            modify_student(self.studenti, 1, 'new_nume', -2)
            assert False
        except ValueError:
            assert True
        try:
            modify_student(self.studenti, 2, 'new_nume', 2)
            assert False
        except Exception:
            assert True


    def test_delete_student(self):
        add_student(self.studenti, 'nume', 1)
        assert delete_student(self.studenti, 1)
        assert not delete_student(self.studenti, 1)


    def test_add_lab(self):
        deadline = datetime.datetime.strptime("25 10 2023", '%d %m %Y')
        add_lab(self.laboratoare, 1, 'descriere', deadline)
        assert len(self.laboratoare.get_all()) == 1
        assert self.laboratoare.get_all()[0].id == 1
        assert self.laboratoare.get_all()[0].descriere == 'descriere'
        assert self.laboratoare.get_all()[0].deadline == deadline
        try:
            add_lab(self.laboratoare, 1, 'descriere', deadline)
            assert False
        except ValueError as ve:
            assert True


    def test_modify_lab(self):
        deadline = datetime.datetime.strptime("25 10 2023", '%d %m %Y')
        deadline_2 = datetime.datetime.strptime("27 10 2023", '%d %m %Y')
        deadline_3 = datetime.datetime.strptime("27 10 2022", '%d %m %Y')
        laborator = add_lab(self.laboratoare, 1, 'descriere', deadline)
        modify_lab(self.laboratoare, 1, 'new_descriere', deadline_2)
        assert self.laboratoare.get_all()[0].descriere == 'new_descriere'
        assert self.laboratoare.get_all()[0].deadline == deadline_2
        try:
            modify_lab(self.laboratoare, 1, 'new_descriere', deadline_3)
            assert False
        except ValueError as ve:
            assert True


    def test_delete_lab(self):
        deadline = datetime.datetime.strptime("25 10 2023", '%d %m %Y')
        laborator = add_lab(self.laboratoare, 1, 'descriere', deadline)
        assert delete_lab(self.laboratoare, 1)
        assert not delete_lab(self.laboratoare, 1)


