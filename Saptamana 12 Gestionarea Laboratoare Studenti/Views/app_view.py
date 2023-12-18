def print_all_students(studenti):
    print("Studenți: ")
    afiseaza_lista(studenti, 0)
    print("-=" * 50 + "\n")


def print_all_labs(laboratoare):
    print("Laboratoare: ")
    afiseaza_lista(laboratoare, 0)
    print("-=" * 50 + "\n")


def afiseaza_lista(lista, i):
    """
    AFISEAZA TOATE ELEMENTELE DINTR-O Lista recursiv
    :param lista: lista de afisat
    :param i: index de afisat
    :return:
    """
    if len(lista) <= i:
        return
    print(lista[i])
    afiseaza_lista(lista, i + 1)


def afiseaza_note(studenti, ind, id):
    """
    Afiseaza notele studentilor la un anumit laborator RECURSIV
    :param studenti:
    :param ind:
    :param id:
    :return:
    """
    if len(studenti) <= ind:
        return
    index_lab = studenti[ind].get_lab_ind(id)
    print(f'{studenti[ind].nume}, {studenti[ind].note[index_lab]}')
    afiseaza_note(studenti,ind+1,id)


def afiseaza_note_studenti(studenti, id):
    print("-=" * 50)
    afiseaza_note(studenti, 0, id)
    print("-=" * 50)


def afiseaza_stud_corigenti(studenti):
    print("-=" * 50)
    for stud in studenti:
        note = ""
        for nota in stud.note:
            note += f" {nota}"
        print(f'{stud.nume},{note}')

    print("-=" * 50)
