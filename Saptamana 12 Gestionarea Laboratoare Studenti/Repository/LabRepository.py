from datetime import datetime

from Domain.Laborator import Laborator
from Domain.lab_validator import validate_lab


class LabRepository:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__laboratoare = []

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
                id, descriere, deadline = [token.strip() for token in line.split(';')]
                id = eval(id)
                deadline = datetime.strptime(deadline,"%d %m %Y")
                laborator = Laborator(id, descriere, deadline)
                validate_lab(laborator, self.__laboratoare)
                self.__laboratoare.append(laborator)

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
            laboratoare = self.__laboratoare
            for laborator in laboratoare:
                id = laborator.id
                descriere = laborator.descriere

                deadline = laborator.deadline


                data = f"{id};{descriere};{deadline.day} {deadline.month} {deadline.year}\n"
                f.write(data)

    def get_all(self):
        """
        returneaza toate locuintele
        :return:
        """
        return self.__laboratoare

    def delete(self, id):
        """
        Sterge client cu id-ul specificat din repository
        :param id:id locuintei de sters
        :return:
        """
        laborator = None
        for i in range(len(self.__laboratoare)):
            if self.__laboratoare[i].id == id:
                return self.__laboratoare.pop(i)
        return False

    def store(self):
        self.__write_to_file()

    def load(self):
        self.__read_from_file()

    def add(self, laborator):
        self.__laboratoare.append(laborator)

    def update(self, laborator):
        index = self.__get_index_from_id(laborator.id)
        if index != -1:
            self.__laboratoare[index] = laborator

    def get_by_id(self, id):
        for laborator in self.__laboratoare:
            if laborator.id == id:
                return laborator

    def __get_index_from_id(self, id):
        for i in range(len(self.__laboratoare)):
            if self.__laboratoare[i].id == id:
                return i
        return -1
