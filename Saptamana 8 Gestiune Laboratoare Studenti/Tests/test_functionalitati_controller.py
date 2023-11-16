import datetime

from Controller.asign_controller import assign_lab, assign_nota
from Controller.crud import add_student, add_lab
from Controller.functionalitati_controller import cauta_student, cauta_laborator, swap_studenti, sort_studenti_nota, \
    sort_studenti_nume, stat_stud_lab, stat_stud_medie_5


def test_cauta_student():
    studenti = []
    add_student(studenti, 'Banciu Horațiu', 211)
    add_student(studenti, 'Darius Horge', 211)
    add_student(studenti, 'Cristian Alexandru', 211)
    assert cauta_student(studenti, None, 1) == studenti[0]
    assert cauta_student(studenti, 'Cristian Alexandru') == studenti[2]
    try:
        cauta_student(studenti, None, 5)
        assert False
    except Exception:
        assert True
    try:
        cauta_student(studenti, 'Anastasia Tudorache')
        assert False
    except Exception:
        assert True


def test_cauta_laborator():
    deadline = datetime.datetime.strptime('25 12 2023','%d %m %Y')
    laboratoare = []
    add_lab(laboratoare,1,'FP',deadline)
    add_lab(laboratoare, 2,'FP2',deadline)
    add_lab(laboratoare, 3,"FP3", deadline)
    assert cauta_laborator(laboratoare,2) == laboratoare[1]
    try:
        cauta_laborator(laboratoare,5)
        assert False
    except Exception :
        assert True

def test_swap_studenti():
    studenti = []
    add_student(studenti,'h',211)
    add_student(studenti,'b',211)
    studenti = swap_studenti(studenti,0,1)
    assert studenti[0].nume == 'b'
    assert studenti[1].nume == 'h'

def test_sortari():
    studenti = []
    laboratoare = []
    add_student(studenti, 'h', 211)
    add_student(studenti, 'd', 211)
    add_student(studenti, 'b', 211)
    add_lab(laboratoare,1,'asdf',datetime.datetime.strptime('25 10 2023','%d %m %Y'))
    assert studenti[1].nume == 'd'
    assert studenti[0].nume == 'h'
    assert studenti[2].nume == 'b'
    assign_lab(studenti,laboratoare,1,None,1)
    assign_lab(studenti,laboratoare,1,None,2)
    assign_lab(studenti, laboratoare, 1, None, 3)

    assign_nota(studenti,laboratoare,1,9,None,1)
    assign_nota(studenti,laboratoare,1,10,None,2)
    assign_nota(studenti, laboratoare, 1, 10, None, 3)
    studenti = sort_studenti_nota(studenti,1)
    assert studenti[0].nume == 'd'
    assert studenti[1].nume == 'b'
    assert studenti[2].nume == 'h'
    studenti = sort_studenti_nume(studenti,1)
    assert studenti[0].nume == 'b'
    assert studenti[1].nume == 'd'
    assert studenti[2].nume == 'h'

def test_stat_stud_lab():
    studenti = []
    laboratoare = []
    add_student(studenti, 'h', 211)
    add_student(studenti, 'd', 211)
    add_student(studenti, 'b', 211)
    add_student(studenti, 'c', 211)
    add_lab(laboratoare, 1, 'asdf', datetime.datetime.strptime('25 10 2023', '%d %m %Y'))

    assign_lab(studenti, laboratoare, 1, None, 1)
    assign_lab(studenti, laboratoare, 1, None, 2)
    assign_lab(studenti, laboratoare, 1, None, 4)

    assign_nota(studenti, laboratoare, 1, 9, None, 1)
    assign_nota(studenti, laboratoare, 1, 10, None, 2)
    assign_nota(studenti, laboratoare, 1, 10, None, 4)
    assert len(studenti) == 4
    studenti_lab = stat_stud_lab(studenti,1)
    assert len(studenti_lab) == 3

    assert studenti_lab[0].note[0] >= studenti_lab[1].note[0] and studenti_lab[0].note[0] > studenti_lab[2].note[0]
    assert studenti_lab[0].nume < studenti_lab[1].nume

def test_stat_stud_medie_5():
    studenti = []
    laboratoare = []
    add_student(studenti, 'a', 211)
    add_student(studenti, 'b', 211)
    add_student(studenti, 'c', 211)
    add_student(studenti, 'd', 211)
    add_lab(laboratoare, 1, 'asdf', datetime.datetime.strptime('25 10 2023', '%d %m %Y'))
    add_lab(laboratoare, 2, 'asdf', datetime.datetime.strptime('25 10 2023', '%d %m %Y'))

    assign_lab(studenti, laboratoare, 1, None, 1)
    assign_lab(studenti, laboratoare, 1, None, 2)
    assign_lab(studenti, laboratoare, 1, None, 3)
    assign_lab(studenti, laboratoare, 1, None, 4)
    assign_lab(studenti, laboratoare, 2, None, 1)
    assign_lab(studenti, laboratoare, 2, None, 2)
    assign_lab(studenti, laboratoare, 2, None, 3)
    assign_lab(studenti, laboratoare, 2, None, 4)

    assign_nota(studenti, laboratoare, 1, 9, None, 1)
    assign_nota(studenti, laboratoare, 1, 2, None, 2)
    assign_nota(studenti, laboratoare, 1, 10, None, 3)
    assign_nota(studenti, laboratoare, 1, 4, None, 4)

    assign_nota(studenti, laboratoare, 2, 9, None, 1)
    assign_nota(studenti, laboratoare, 2, 2, None, 2)
    assign_nota(studenti, laboratoare, 2, 10, None, 3)
    assign_nota(studenti, laboratoare, 2, 4, None, 4)

    corigenti = stat_stud_medie_5(studenti)
    assert corigenti[0].nume == 'b'
    assert corigenti[0].medie_note() == 2
    assert corigenti[1].nume == 'd'
    assert corigenti[1].medie_note() == 4

def test_func_controller():
    test_cauta_student()
    test_cauta_laborator()
    test_swap_studenti()
    test_sortari()
    test_stat_stud_lab()
    test_stat_stud_medie_5()
