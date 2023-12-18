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
    :return: laborator asau Exception
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
    for stud in studenti.get_all():
        if lab_id in stud.laboratoare:
            lst.append(stud)
    return lst


def swap_studenti(list_studenti, pos1, pos2):
    """
    Interschimba_2_studenti
    :param list_studenti: list studenti
    :param pos1:
    :param pos2:
    :return: lista modificata
    """
    list_studenti[pos1], list_studenti[pos2] = list_studenti[pos2], list_studenti[pos1]



def stat_stud_lab(studenti, lab_id):
    studenti_lab = get_studenti_lab(studenti, lab_id)
    if studenti_lab != []:
        quick_sorted(studenti_lab, 0, len(studenti_lab) - 1, lab_id, key=lambda x: x.note[x.get_lab_ind(lab_id)],
                     reverse=True)
        gnome_sorted(studenti_lab, lab_id, key=lambda x: x.note[x.get_lab_ind(lab_id)], key2=lambda x: x.nume)
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
    studenti_lab = stat_stud_lab(studenti, lab_id)
    length = len(studenti_lab)
    length //= 10
    return studenti_lab[0:length]


def partition(studenti_lab, st, dr, lab_id, key, reverse):

    index_curent = st
    if lab_id is not None:
        pivot = key(studenti_lab[dr])
        if not reverse:
            for i in range(st, dr):
                if key(studenti_lab[i]) <= pivot:
                    swap_studenti(studenti_lab, i, index_curent)
                    index_curent += 1
        else:
            for i in range(st, dr):
                if key(studenti_lab[i]) >= pivot:
                    swap_studenti(studenti_lab, i, index_curent)
                    index_curent += 1

    else:
        pivot = studenti_lab[dr]
        if not reverse:
            for i in range(st, dr):
                if studenti_lab[i] <= pivot:
                    swap_studenti(studenti_lab,i,index_curent)
                    index_curent += 1
        else:
            for i in range(st,dr):
                if studenti_lab[i] >= pivot:
                    swap_studenti(studenti_lab,i,index_curent)
                    index_curent += 1
    swap_studenti(studenti_lab, dr, index_curent)
    return index_curent


def quick_sorted(studenti_lab, st, dr, lab_id=None, key=None, reverse=False):
    """
    ANALIZA COMPLEXITATE:
    Caz-ul mediu: aceasta metoda de sortare are o complexitate N * log(N)
    Worst Case: Lista este deja sortata, in acest caz metoda de sortare are o complexitate N*N
    Sorteaza cu quick sort lista
    :param studenti_lab: lista studenti
    :param st:stanga
    :param dr:dreapta
    :param lab_id:id lab de sortat
    :param key: functie dupa care se sorteaza
    :param reverse:Ordinea
    :return:
    """
    if st <= dr:
        pindex = partition(studenti_lab, st, dr, lab_id, key, reverse)
        quick_sorted(studenti_lab, st, pindex - 1, lab_id, key, reverse)
        quick_sorted(studenti_lab, pindex + 1, dr, lab_id, key, reverse)


def gnome_sorted(studenti_lab, lab_id=None, key=None, key2=None, reverse=False):
    """
    Sorteaza cu gnome sort lista de studenti in functie de nume
    :param studenti_lab: Lista studenti
    :param key: functia obtinere nota
    :param key2: functia obtinere nume
    :param lab_id: id lab cu nota
    :param reverse: crescator/descrescator
    :return: lista sortata in functie de nota alfabetic
    """
    # Sortare dupa KEY
    i = 1
    if lab_id is not None:
        if not reverse:  # Crescator
            while i < len(studenti_lab):
                if key(studenti_lab[i]) == key(studenti_lab[i - 1]) and key2(studenti_lab[i]) < key2(
                        studenti_lab[i - 1]):
                    swap_studenti(studenti_lab, i, i - 1)
                    i -= 1
                else:
                    i += 1
        else:  # DEscrescator
            while i < len(studenti_lab):
                if key(studenti_lab[i]) == key(studenti_lab[i - 1]) and key2(studenti_lab[i]) > key2(
                        studenti_lab[i - 1]):
                    swap_studenti(studenti_lab, i, i - 1)
                    i -= 1
                else:
                    i += 1
    # SORTARE Normala
    else:
        if not reverse:  # Crescator
            while i < len(studenti_lab):
                if studenti_lab[i] < studenti_lab[i - 1]:
                    swap_studenti(studenti_lab, i, i - 1)
                    i -= 1
                else:
                    i += 1
        else:  # DEscrescator
            while i < len(studenti_lab):
                if studenti_lab[i] > studenti_lab[i - 1]:
                    swap_studenti(studenti_lab, i, i - 1)
                    i -= 1
                else:
                    i += 1
