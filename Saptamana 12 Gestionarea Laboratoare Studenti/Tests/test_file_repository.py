from Repository.LabRepository import LabRepository
from Repository.StudentiRepository import StudentRepository
from Repository.file_repository import create_x_students, create_x_labs
import unittest

class file_repository_test(unittest.TestCase):
    def setUp(self):
        self.lab_repository = LabRepository("Data/test_Lab.txt")
        self.students_repository = StudentRepository("Data/test_student.txt")

    def test_create_x_laboratoare(self):
        create_x_labs(10, self.lab_repository)
        assert len(self.lab_repository.get_all()) == 10


    def test_create_x_students(self):

        create_x_labs(10, self.lab_repository)
        create_x_students(10, self.students_repository, self.lab_repository)
        assert (len(self.students_repository.get_all())) == 10
