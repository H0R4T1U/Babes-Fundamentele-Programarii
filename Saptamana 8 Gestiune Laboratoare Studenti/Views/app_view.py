def print_all_students(studenti):
    print("Studenți: ")
    for student in studenti:
        print(student)
    print("-=" * 50 + "\n")


def print_all_labs(laboratoare):
    print("Laboratoare: ")
    for lab in laboratoare:
        print(lab)
    print("-=" * 50 + "\n")


def afiseaza_note_studenti(studenti, id):
    print("-=" * 50)
    for stud in studenti:
        ind = stud.get_lab_ind(id)
        print(f'{stud.nume}, {stud.note[ind]}')
    print("-=" * 50)

def afiseaza_stud_corigenti(studenti):
    print("-=" * 50)
    for stud in studenti:
        note = ""
        for nota in stud.note:
            note += f" {nota}"
        print(f'{stud.nume},{note}')

    print("-=" * 50)