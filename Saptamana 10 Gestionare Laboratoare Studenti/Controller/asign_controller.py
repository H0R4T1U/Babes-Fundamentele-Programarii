from Controller.crud import get_student_by_id, get_student_by_name, get_lab_by_id


def assign_lab(studenti, laboratoare, lab_id, nume_student=None, id_student=None):
    """
    Asignează un laborator la student
    :param studenti:lista studenti
    :param laboratoare: lista laboratoare
    :param lab_id: id laborator
    :param nume_student: nume student
    :param id_student:id student
    :return: Asigneaza laborator la student sau Exception
    """
    try:
        stud = __valideaza_date(studenti, laboratoare, lab_id, nume_student, id_student)
    except Exception as ex:
        raise Exception(str(ex) + "Laboratorul nu a fost asginat!\n")
    else:
        if lab_id not in stud.laboratoare:
            stud.laboratoare.append(lab_id)
            stud.note.append(0)
        else:
            raise Exception("Laboratorul este deja asignat!\n")


def assign_nota(studenti, laboratoare, lab_id, nota, student_name=None, student_id=None):
    try:
        stud = __valideaza_date(studenti, laboratoare, lab_id, student_name, student_id, nota)
    except Exception as ex:
        raise Exception(str(ex) + "Nota nu a fost asignata!\n")
    else:
        if lab_id in stud.laboratoare:
            index = stud.get_lab_ind(lab_id)
            stud.note[index] = nota
        else:
            assign_lab(studenti, laboratoare, lab_id, student_name, student_id)
            stud.note[-1] = nota


def __valideaza_date(studenti, laboratoare, lab_id, student_name=None, student_id=None, nota=None):
    """
    verifica datele introduse si returneaza studentul
    :param studenti:
    :param laboratoare:
    :param lab_id:
    :param student_name:
    :param student_id:
    :param nota:
    :return:type Student
    """
    msg = ""
    try:
        get_lab_by_id(laboratoare, lab_id)
    except Exception as ex:
        msg += str(ex)

    if student_name is not None:
        try:
            stud = get_student_by_name(studenti, student_name)
        except Exception as ex:
            msg += str(ex)
    elif student_id is not None:
        try:
            stud = get_student_by_id(studenti, student_id)
        except Exception as ex:
            msg += Exception(str(ex))
    if nota is not None:
        if nota <= 0 or nota > 10:
            msg += "Nota introdusă este invalidă!\n"
    if msg != "":
        raise Exception(msg)
    else:
        return stud
