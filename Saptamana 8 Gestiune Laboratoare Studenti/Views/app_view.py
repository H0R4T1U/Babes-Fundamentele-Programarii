from datetime import datetime

from Domain.Laborator import get_nr_lab,get_descriere,get_deadline


def print_all_students(studenti):
    
    print("Studenți: ")
    for student in studenti:
        print(f"{student.id}. {student.nume} grupa {student.grupa}")

    print("-="*50+"\n")
def print_all_labs(laboratoare):
    print("Laboratoare: ")
    for lab in laboratoare:
        timp = get_deadline(lab)
        print(f"{get_nr_lab(lab)}. {get_descriere(lab)}, {timp.day}.{timp.month}.{timp.year}")
    print("-=" * 50 + "\n")