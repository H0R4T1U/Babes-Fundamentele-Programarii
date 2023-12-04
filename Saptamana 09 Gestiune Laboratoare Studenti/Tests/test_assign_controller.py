import datetime

from Controller.asign_controller import assign_lab, assign_nota
from Controller.crud import add_student, add_lab
def test_asign_lab():
    studenti = []
    laboratoare = []
    add_student(studenti, 'Banciu Horatiu', 211)
    add_lab(laboratoare, 1, "FP", datetime.datetime.strptime('31 12 2023', '%d %m %Y'))
    add_lab(laboratoare, 2, "FP", datetime.datetime.strptime('31 12 2023', '%d %m %Y'))
    assert studenti[0].laboratoare == []
    assign_lab(studenti, laboratoare, 1, 'Banciu Horatiu')
    assert studenti[0].laboratoare == [1]
    assign_lab(studenti, laboratoare, 2, None, 1)
    assert studenti[0].laboratoare == [1, 2]

    try:
        assign_lab(studenti, laboratoare, 3, 'Banciu Horatiu')
        assert False
    except Exception:
        assert True
    try:
        assign_lab(studenti, laboratoare, 1, 'Alex')
        assert False
    except Exception:
        assert True
    try:
        assign_lab(studenti, laboratoare, 1, None, 2)
        assert False
    except Exception:
        assert True
    try:
        assign_lab(studenti, laboratoare, 1, None, 1)
        assert False
    except Exception as ex:
        assert True


def test_assign_nota():
    studenti = []
    laboratoare = []
    add_student(studenti, 'Banciu Horatiu', 211)
    add_lab(laboratoare, 1, "FP", datetime.datetime.strptime('25 12 2023', '%d %m %Y'))
    add_lab(laboratoare, 2, "FP", datetime.datetime.strptime('31 12 2023', '%d %m %Y'))
    assert studenti[0].laboratoare == []
    assert studenti[0].note == []
    assign_nota(studenti, laboratoare, 1, 10, 'Banciu Horatiu')
    assert studenti[0].laboratoare == [1]
    assert studenti[0].note == [10]
    assign_lab(studenti, laboratoare, 2, None, 1)
    assign_nota(studenti, laboratoare, 2, 9, None, 1)
    assert studenti[0].laboratoare == [1, 2]
    assert studenti[0].note == [10, 9]

def test_assign_controller():
    test_asign_lab()
    test_assign_nota()