
def valideaza_student(student, studenti):
    """
    Functia valideaza un student
    :param student:
    :param studenti:
    :return:
    """
    msg = ""
    if student.id in [stud.id for stud in studenti]:
        msg += "Id-ul exista deja!\n"
    if student.nume == "":
        msg += "Numele nu poate fi vid!\n"
    if student.grupa < 0:
        msg += "Grupa nu poate fi negativa!\n"
    if student.grupa > 999:
        msg += "Grupa nu poate fi mai mare decat 999!\n"
    if student.grupa == 0:
        msg += "Grupa nu poate fi 0!\n"
    if msg != "":
        raise ValueError(msg)
    return True
