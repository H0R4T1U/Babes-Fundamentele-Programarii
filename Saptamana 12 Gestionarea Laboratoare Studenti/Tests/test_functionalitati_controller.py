import datetime
import unittest
from Controller.asign_controller import assign_lab, assign_nota
from Controller.crud import add_student, add_lab
from Controller.functionalitati_controller import (cauta_student, cauta_laborator, swap_studenti
, stat_stud_lab, stat_stud_medie_5, stat_stud_lab_10, quick_sorted, gnome_sorted)
from Repository.LabRepository import LabRepository
from Repository.StudentiRepository import StudentRepository
from Repository.file_repository import create_x_labs, create_x_students


class TestFunctionalitatiController(unittest.TestCase):
    def setUp(self):
        self.studenti = StudentRepository("Data/test_studenti")
        self.lab_repository = LabRepository("Data/test_Lab")

    def test_cauta_student(self):
        add_student(self.studenti, 'Banciu Horațiu', 211)
        add_student(self.studenti, 'Darius Horge', 211)
        add_student(self.studenti, 'Cristian Alexandru', 211)
        assert cauta_student(self.studenti, None, 1) == self.studenti.get_all()[0]
        assert cauta_student(self.studenti, 'Cristian Alexandru') == self.studenti.get_all()[2]
        try:
            cauta_student(self.studenti, None, 5)
            assert False
        except Exception:
            assert True
        try:
            cauta_student(self.studenti, 'Anastasia Tudorache')
            assert False
        except Exception:
            assert True


    def test_cauta_laborator(self):
        deadline = datetime.datetime.strptime('25 12 2023', '%d %m %Y')
        add_lab(self.lab_repository, 1, 'FP', deadline)
        add_lab(self.lab_repository, 2, 'FP2', deadline)
        add_lab(self.lab_repository, 3, "FP3", deadline)
        assert cauta_laborator(self.lab_repository, 2) == self.lab_repository.get_all()[1]
        try:
            cauta_laborator(self.lab_repository, 5)
            assert False
        except Exception:
            assert True


    def test_swap_studenti(self):
        add_student(self.studenti, 'h', 211)
        add_student(self.studenti, 'b', 211)
        swap_studenti(self.studenti.get_all(), 0, 1)
        assert self.studenti.get_all()[0].nume == 'b'
        assert self.studenti.get_all()[1].nume == 'h'


    def test_stat_stud_lab(self):

        add_student(self.studenti, 'h', 211)
        add_student(self.studenti, 'd', 211)
        add_student(self.studenti, 'b', 211)
        add_student(self.studenti, 'c', 211)
        add_lab(self.lab_repository, 1, 'asdf', datetime.datetime.strptime('25 10 2023', '%d %m %Y'))

        assign_lab(self.studenti, self.lab_repository, 1, None, 1)
        assign_lab(self.studenti, self.lab_repository, 1, None, 2)
        assign_lab(self.studenti, self.lab_repository, 1, None, 4)

        assign_nota(self.studenti, self.lab_repository, 1, 9, None, 1)
        assign_nota(self.studenti, self.lab_repository, 1, 10, None, 2)
        assign_nota(self.studenti, self.lab_repository, 1, 10, None, 4)
        assert len(self.studenti.get_all()) == 4
        studenti_lab = stat_stud_lab(self.studenti, 1)
        assert len(studenti_lab) == 3

        assert studenti_lab[0].note[0] >= studenti_lab[1].note[0] and studenti_lab[0].note[0] > studenti_lab[2].note[0]
        assert studenti_lab[0].nume < studenti_lab[1].nume


    def test_stat_stud_medie_5(self):

        add_student(self.studenti, 'a', 211)
        add_student(self.studenti, 'b', 211)
        add_student(self.studenti, 'c', 211)
        add_student(self.studenti, 'd', 211)
        add_lab(self.lab_repository, 1, 'asdf', datetime.datetime.strptime('25 10 2023', '%d %m %Y'))
        add_lab(self.lab_repository, 2, 'asdf', datetime.datetime.strptime('25 10 2023', '%d %m %Y'))

        assign_lab(self.studenti, self.lab_repository, 1, None, 1)
        assign_lab(self.studenti, self.lab_repository, 1, None, 2)
        assign_lab(self.studenti, self.lab_repository, 1, None, 3)
        assign_lab(self.studenti, self.lab_repository, 1, None, 4)
        assign_lab(self.studenti, self.lab_repository, 2, None, 1)
        assign_lab(self.studenti, self.lab_repository, 2, None, 2)
        assign_lab(self.studenti, self.lab_repository, 2, None, 3)
        assign_lab(self.studenti, self.lab_repository, 2, None, 4)

        assign_nota(self.studenti, self.lab_repository, 1, 9, None, 1)
        assign_nota(self.studenti, self.lab_repository, 1, 2, None, 2)
        assign_nota(self.studenti, self.lab_repository, 1, 10, None, 3)
        assign_nota(self.studenti, self.lab_repository, 1, 4, None, 4)

        assign_nota(self.studenti, self.lab_repository, 2, 9, None, 1)
        assign_nota(self.studenti, self.lab_repository, 2, 2, None, 2)
        assign_nota(self.studenti, self.lab_repository, 2, 10, None, 3)
        assign_nota(self.studenti, self.lab_repository, 2, 4, None, 4)

        corigenti = stat_stud_medie_5(self.studenti.get_all())
        assert corigenti[0].nume == 'b'
        assert corigenti[0].medie_note() == 2
        assert corigenti[1].nume == 'd'
        assert corigenti[1].medie_note() == 4


    def test_sortari(self):

        create_x_labs(1, self.lab_repository)
        create_x_students(100, self.studenti, self.lab_repository)
        lista_stud = self.studenti.get_all()
        quick_sorted(lista_stud, 0, 99, 1, key=lambda x: x.note[x.get_lab_ind(1)], reverse=True)
        gnome_sorted(lista_stud, 1, key=lambda x: x.note[x.get_lab_ind(1)], key2=lambda x: x.nume)
        assert (lista_stud[0].note >= lista_stud[1].note and lista_stud[0].nume <= lista_stud[1].nume)
        assert (lista_stud[0].note >= lista_stud[2].note and lista_stud[0].nume <= lista_stud[2].nume)


    def test_stat_stud_lab_10(self):
        create_x_labs(1, self.lab_repository)
        create_x_students(100, self.studenti, self.lab_repository)
        stud_lab = stat_stud_lab_10(self.studenti, 1)
        assert len(stud_lab) == 10
        assert stud_lab[0].nume < stud_lab[1].nume


