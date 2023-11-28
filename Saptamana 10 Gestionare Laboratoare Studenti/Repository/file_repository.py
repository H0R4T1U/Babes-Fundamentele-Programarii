import datetime
import random
import string

from Controller.asign_controller import assign_lab, assign_nota
from Controller.crud import add_lab, add_student


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


def create_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def create_random_number(min, max):
    return random.randrange(min, max)


def create_x_students(x, studenti, laboratoare):
    for i in range(1, x + 1):
        nume = create_random_string(10)
        grupa = create_random_number(1, 999)
        add_student(studenti, nume, grupa)
        for j in range(1,len(laboratoare) + 1):
            nota = random.randrange(1, 11)
            try:
                assign_lab(studenti, laboratoare, j, None, i)
                assign_nota(studenti, laboratoare, j, nota, None, i)
            except Exception as ex:
                continue


def create_x_labs(x, laboratoare):
    start = datetime.datetime.strptime('1 1 2023', '%d %m %Y')
    stop = datetime.datetime.strptime('31 12 2024', '%d %m %Y')
    for i in range(len(laboratoare) +1, x + 1):
        descriere = create_random_string(7)
        data = random_date(start, stop)
        add_lab(laboratoare, i, descriere, data)
