from Domain.Student import Student
from Domain.student_validator import valideaza_student


class StudentRepository:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__studenti = []

    @property
    def studenti(self):
        return self.__studenti
    @studenti.setter
    def studenti(self,new_studenti):
        self.__studenti = new_studenti

    def __read_from_file(self):
        """
        Citire din fisier
        :return: lista cu locuinte
        """
        try:
            f = open(self.__file_name, 'r')
        except IOError:
            print("Fișier Corupt/Nu există")
        else:
            lines = f.readlines()
            for line in lines:
                id, nume, grupa, laboratoare, note = [token.strip() for token in line.split(';')]
                id = eval(id)
                grupa = eval(grupa)
                laboratoare = eval(laboratoare)
                note = eval(note)
                student = Student(id, nume, grupa, laboratoare, note)
                valideaza_student(student, self.__studenti)
                self.__studenti.append(student)

    def __write_to_file(self):
        """
        Scriere in fisier
        :return:
        """
        try:
            f = open(self.__file_name, 'w')
        except IOError:
            print("Fișier Corupt/Nu există")
        else:
            studenti = self.__studenti
            for student in studenti:
                id = student.id
                nume = student.nume

                grupa = student.grupa
                laboratoare = student.laboratoare

                note = student.note
                data = f"{id};{nume};{grupa};{laboratoare};{note}\n"
                f.write(data)

    def get_all(self):
        """
        returneaza toate locuintele
        :return:
        """
        return self.__studenti

    def delete(self, id):
        """
        Sterge client cu id-ul specificat din repository
        :param id:id locuintei de sters
        :return:
        """
        for i in range(len(self.__studenti)):
            if self.__studenti[i].id == id:
                self.__studenti.pop(i)
                return True
        return False

    def store(self):
        self.__write_to_file()

    def load(self):
        self.__read_from_file()

    def add(self, student):
        self.__studenti.append(student)

    def update(self, student):
        index = self.__get_index_from_id(student.id)
        if index != -1:
            self.__studenti[index] = student

    def get_by_id(self, id):
        for student in self.__studenti:
            if student.id == id:
                return student
        return -1

    def __get_index_from_id(self, id):
        for i in range(len(self.__studenti)):
            if self.__studenti[i].id == id:
                return i
        return -1
