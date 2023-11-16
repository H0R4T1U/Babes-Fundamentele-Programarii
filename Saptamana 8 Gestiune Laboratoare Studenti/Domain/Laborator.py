class Laborator:
    def __init__(self, id_lab, descriere, deadline):
        self.__id = id_lab
        self.__descriere = descriere
        self.__deadline = deadline

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id):
        self.__id = new_id

    @property
    def descriere(self):
        return self.__descriere

    @descriere.setter
    def descriere(self, new_desc):
        self.__descriere = new_desc

    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, n_deadline):
        self.__deadline = n_deadline

    def __str__(self):
        return f"{self.id}. {self.descriere}, {self.deadline.day}.{self.deadline.month}.{self.deadline.year}"

