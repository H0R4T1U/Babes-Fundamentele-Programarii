from Controller.crud import get_student_by_id, get_student_by_name, get_lab_by_id


def assign_lab(studenti,laboratoare,lab_id,nume_student=None,id_student=None):
    """
    Asignează un laborator la student
    :param studenti:
    :param laboratoare:
    :param lab_id:
    :param nume_student:
    :param id_student:
    :return:
    """
    try:
        get_lab_by_id(laboratoare,lab_id)
    except Exception as ex:
        print(ex)
        print("Laboratorul nu a putut fi asignat!")
    else:
        if id_student is not None:
            try:
                get_student_by_id(studenti,id_student).laboratoare.append(lab_id)
            except Exception as ex:
                print(ex)
                print("Laboratorul nu a putut fi asignat!")
            else:
                print("Laborator asignat cu succes!")
        else:
            try:
                get_student_by_name(studenti, nume_student).laboratoare.append(lab_id)
            except Exception as ex:
                print(ex)
                print("Laboratorul nu a putut fi asignat!")
            else:
                print("Laborator asignat cu succes!")
            #VERIFICĂ DACĂ LABORATUL ESTE DEJA ASIGNAT!!!!

