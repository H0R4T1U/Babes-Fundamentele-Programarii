
import unittest

from Domain.Laborator import Laborator
from Domain.Student import Student


class DomainTest(unittest.TestCase):

    def test_creaza_lab(self):
        """
         Functia testeaza creeaza_lab
        :return:
        """
        lab = Laborator(1, 'descriere', 'deadline')
        self.assertEqual(lab.id, 1)
        self.assertEqual(lab.descriere, 'descriere')
        self.assertEqual(lab.deadline, 'deadline')

    def test_lab_seters(self):
        """
        Functia testeaza set_deadline si set_descriere
        :return:
        """
        lab = Laborator(1, 'descriere', 'deadline')
        lab.deadline = 'new_deadline'
        lab.descriere = 'new_descriere'
        lab.id = 2

        self.assertEqual(lab.id, 2)
        self.assertEqual(lab.descriere, 'new_descriere')
        self.assertEqual(lab.deadline, 'new_deadline')

    def test_create_student(self):
        """
        Functia testeaza creeaza_student
        :return:
        """
        student = Student(1, 'nume', 1)
        self.assertEqual(student.id, 1)
        self.assertEqual(student.nume, 'nume')
        self.assertEqual(student.grupa, 1)
        self.assertEqual(student.note, [])
        self.assertEqual(student.laboratoare, [])
        assert (student.id == 1)
        assert (student.nume == 'nume')
        assert (student.grupa == 1)
        assert (student.laboratoare == [])
        assert (student.note == [])

    def test_student_seters(self):
        """
        Functia testeaza set_id, set_nume, set_grupa
        :return:
        """
        student = Student(1, 'nume', 1)
        student.id = 2
        student.nume = "new_nume"
        student.grupa = 3

        self.assertEqual(student.id, 2)
        self.assertEqual(student.nume, 'new_nume')
        self.assertEqual(student.grupa, 3)

