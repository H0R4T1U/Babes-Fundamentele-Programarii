class Student:
    def __init__(self, id, nume, grupa, laboratoare=None, note=None):
        if laboratoare is None:
            laboratoare = []
        if note is None:
            note = []
        self.__id = id
        self.__nume = nume
        self.__grupa = grupa
        self.__laboratoare = laboratoare
        self.__note = note

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id):
        self.__id = new_id

    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, new_name):
        self.__nume = new_name

    @property
    def grupa(self):
        return self.__grupa

    @grupa.setter
    def grupa(self, grupa_noua):
        self.__grupa = grupa_noua

    @property
    def laboratoare(self):
        return self.__laboratoare

    @laboratoare.setter
    def laboratoare(self, new_labs):
        self.__laboratoare = new_labs

    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note_noi):
        self.__note = note_noi

    def __str__(self):
        return f"{self.id}. {self.nume} grupa {self.grupa}"

    def __lt__(self, other):
        return self.id < other.id

    def __le__(self, other):
        return self.id <= other.id

    def __gt__(self, other):
        return self.id > other.id

    def __ge__(self, other):
        return self.id >= other.id


    def get_lab_ind(self, lab_id):
        for i in range(len(self.laboratoare)):
            if self.laboratoare[i] == lab_id:
                return i
        return -1

    def medie_note(self):
        sum = 0
        i = 0
        for i in range(len(self.note)):
            sum += self.note[i]
        return sum / (i + 1)
