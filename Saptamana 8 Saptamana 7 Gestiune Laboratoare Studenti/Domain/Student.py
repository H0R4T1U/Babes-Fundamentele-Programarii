class Student:
    def __init__(self, id, nume, grupa):
        self.__id = id
        self.__nume = nume
        self.__grupa = grupa
        self.__laboratoare = []
        self.__note = []

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
    def note(self,note_noi):
        self.__note = note_noi


