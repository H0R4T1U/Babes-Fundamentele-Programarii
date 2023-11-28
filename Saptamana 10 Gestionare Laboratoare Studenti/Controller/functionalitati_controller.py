from Controller.crud import get_student_by_name, get_student_by_id, get_lab_by_id


def cauta_student(studenti, nume_student=None, id_student=None):
    """
    Cauta un student in lista de studenti
    :param studenti: lista de studenti
    :param nume_student: numele studentului
    :param id_student: id student
    :return: studentul sau Exception
    """
    if nume_student is not None:
        return get_student_by_name(studenti, nume_student)
    if id_student is not None:
        return get_student_by_id(studenti, id_student)


def cauta_laborator(laboratoare, id_laborator):
    """
    Caută un laborator in lista de laboratoare
    :param laboratoare: lista laboratoare
    :param id_laborator: id laborator cautat
    :return: laborator sau Exception
    """
    return get_lab_by_id(laboratoare, id_laborator)


def get_studenti_lab(studenti, lab_id):
    """
    Functie de gasire a tuturor studentilor de la un anumit laborator
    :param studenti: lista studenti
    :param lab_id: id laborator
    :return: lista cu studenti de la laborator
    """
    lst = []
    for stud in studenti:
        if lab_id in stud.laboratoare:
            lst.append(stud)
    return lst


def swap_studenti(list_studenti, pos1, pos2):
    """
    Interschimba_2_studenti
    :param list_studenti:
    :param pos1:
    :param pos2:
    :return: lista modificata
    """
    list_studenti[pos1], list_studenti[pos2] = list_studenti[pos2], list_studenti[pos1]
    return list_studenti


def sort_studenti_nume(studenti_lab, lab_id):
    """
    SORTEAZA STUDENTI CRESCATOR DUPA NUME, SI NOTE
    :param studenti_lab: LISTA STUDENTI SORTATA DESC DUPA NOTA
    :param lab_id: ID LAB
    :return: LISTA STUDENTI SORTATA
    """
    for i in range(len(studenti_lab)):
        for j in range(len(studenti_lab) - 1):
            ind_lab = studenti_lab[j].get_lab_ind(lab_id)
            ind_lab2 = studenti_lab[j + 1].get_lab_ind(lab_id)
            if studenti_lab[j].note[ind_lab] == studenti_lab[j + 1].note[ind_lab2] and studenti_lab[j].nume > \
                    studenti_lab[j + 1].nume:
                swap_studenti(studenti_lab, j, j + 1)
    return studenti_lab


def sort_studenti_nota(studenti_lab, lab_id):
    for i in range(len(studenti_lab)):
        for j in range(len(studenti_lab) - 1):
            ind_lab = studenti_lab[j].get_lab_ind(lab_id)
            ind_lab2 = studenti_lab[j + 1].get_lab_ind(lab_id)
            if studenti_lab[j].note[ind_lab] < studenti_lab[j + 1].note[ind_lab2]:
                swap_studenti(studenti_lab, j, j + 1)
    return studenti_lab


def stat_stud_lab(studenti, lab_id):
    studenti_lab = get_studenti_lab(studenti, lab_id)
    if studenti_lab != []:
        studenti_lab = sort_studenti_nota(studenti_lab, lab_id)
        studenti_lab = sort_studenti_nume(studenti_lab, lab_id)
        return studenti_lab
    else:
        raise Exception("Nu Există nici-un student participant la acest laborator!\n")


def stat_stud_medie_5(studenti):
    st_list = []
    for stud in studenti:
        if stud.medie_note() < 5:
            st_list.append(stud)
    if st_list != []:
        return st_list
    else:
        raise Exception("Nu există nici-un student Corigent!")


def stat_stud_lab_10(studenti, lab_id):
    studenti_lab = stat_stud_lab(studenti,lab_id)
    length = len(studenti_lab)
    length //= 10
    return studenti_lab[0:length]
