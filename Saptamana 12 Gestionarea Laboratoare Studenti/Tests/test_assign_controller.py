import datetime
import unittest
from Controller.asign_controller import assign_lab, assign_nota
from Controller.crud import add_student, add_lab
from Repository.LabRepository import LabRepository
from Repository.StudentiRepository import StudentRepository


class TestAssignController(unittest.TestCase):
    def setUp(self):
        self.studenti = StudentRepository("Data/test_studenti.txt")
        self.laboratoare = LabRepository("Data/test_Lab.txt")

    def test_asign_lab(self):
        add_student(self.studenti, 'Banciu Horatiu', 211)
        add_lab(self.laboratoare, 1, "FP", datetime.datetime.strptime('31 12 2023', '%d %m %Y'))
        add_lab(self.laboratoare, 2, "FP", datetime.datetime.strptime('31 12 2023', '%d %m %Y'))
        assert self.studenti.get_all()[0].laboratoare == []
        assign_lab(self.studenti, self.laboratoare, 1, 'Banciu Horatiu')
        assert self.studenti.get_all()[0].laboratoare == [1]
        assign_lab(self.studenti, self.laboratoare, 2, None, 1)
        assert self.studenti.get_all()[0].laboratoare == [1, 2]

        try:
            assign_lab(self.studenti, self.laboratoare, 3, 'Banciu Horatiu')
            assert False
        except Exception:
            assert True
        try:
            assign_lab(self.studenti, self.laboratoare, 1, 'Alex')
            assert False
        except Exception:
            assert True
        try:
            assign_lab(self.studenti, self.laboratoare, 1, None, 2)
            assert False
        except Exception:
            assert True
        try:
            assign_lab(self.studenti, self.laboratoare, 1, None, 1)
            assert False
        except Exception as ex:
            assert True

    def test_assign_nota(self):
        add_student(self.studenti, 'Banciu Horatiu', 211)
        add_lab(self.laboratoare, 1, "FP", datetime.datetime.strptime('25 12 2023', '%d %m %Y'))
        add_lab(self.laboratoare, 2, "FP", datetime.datetime.strptime('31 12 2023', '%d %m %Y'))
        assert self.studenti.get_all()[0].laboratoare == []
        assert self.studenti.get_all()[0].note == []
        assign_nota(self.studenti, self.laboratoare, 1, 10, 'Banciu Horatiu')
        assert self.studenti.get_all()[0].laboratoare == [1]
        assert self.studenti.get_all()[0].note == [10]
        assign_lab(self.studenti, self.laboratoare, 2, None, 1)
        assign_nota(self.studenti, self.laboratoare, 2, 9, None, 1)
        assert self.studenti.get_all()[0].laboratoare == [1, 2]
        assert self.studenti.get_all()[0].note == [10, 9]
