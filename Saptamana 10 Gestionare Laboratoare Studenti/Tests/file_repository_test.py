from Repository.file_repository import create_x_students, create_x_labs




def test_create_x_laboratoare():
    laboratoare = []
    create_x_labs(10,laboratoare)
    assert len(laboratoare) == 10

def test_create_x_students():
    studenti = []
    laboratoare = []
    create_x_labs(10,laboratoare)
    create_x_students(10, studenti,laboratoare)
    assert (len(studenti)) == 10


def test_all_repositories():
    test_create_x_laboratoare()
    test_create_x_students()
