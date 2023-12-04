from Domain.Student import get_grupa, get_id, get_nume


def valideaza_student(student, studenti):
    """
    Functia valideaza un student
    :param student:
    :param studenti:
    :return:
    """
    msg = ""
    if get_id(student) in [get_id(stud) for stud in studenti]:
        msg += "Id-ul exista deja!\n"
    if get_nume(student) == "":
        msg += "Numele nu poate fi vid!\n"
    if get_grupa(student) < 0:
        msg += "Grupa nu poate fi negativa!\n"
    if get_grupa(student) > 999:
        msg += "Grupa nu poate fi mai mare decat 999!\n"
    if get_grupa(student) == 0:
        msg += "Grupa nu poate fi 0!\n"
    if msg != "":
        raise ValueError(msg)
    return True