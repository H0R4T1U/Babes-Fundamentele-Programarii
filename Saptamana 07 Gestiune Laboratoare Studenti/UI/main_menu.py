from Controller.crud import add_student, modify_student, delete_student, add_lab, modify_lab, delete_lab
from Utility.utility import read_number, cls, read_date
from Views.app_view import print_all_students, print_all_labs


def print_main_menu():
    print("1. Meniu Adăugări/Modificări")
    print("2. Meniu Ștergeri")
    print("A. Afiseaza studenti")
    print("Q. Exit")


def print_add_menu():
    print("1. Adaugă student")
    print("2. Modifică student")
    print("3. Adaugă laborator")
    print("4. Modifică laborator")
    print("5. Asignează student la laborator")
    print("6. Asignează notă studentului la laborator")
    print("q. Back")


def add_student_ui(studenti):
    nume = input("Nume:")
    grupa = read_number("Grupa:",int, "Grupa trebuie sa fie un numar intreg")
    add_student(studenti, nume, grupa)


def modify_student_ui(studenti):
    id = read_number("Id:", int, "Id-ul trebuie sa fie un numar intreg")
    nume = input("Nume nou:")
    grupa = read_number("Grupa noua:", int, "Grupa trebuie sa fie un numar intreg")

    if modify_student(studenti, id ,nume, grupa):
        print("Student modificat cu succes!")
    else:
        print("Studentul nu a fost Modificat!")


def add_lab_ui(laboratoare):
    nr_lab = read_number("Numar laborator:", int, "Numarul laboratorului trebuie sa fie un numar intreg")
    descriere = input("Descriere:")
    deadline = read_date("Deadline:", "%d %m %Y", "Deadline invalid!")
    add_lab(laboratoare, nr_lab, descriere, deadline)


def modify_lab_ui(laboratoare):
    nr_lab = read_number("Numar laborator:", int, "Numarul laboratorului trebuie sa fie un numar intreg")
    descriere = input("Descriere noua:")
    deadline = read_date("Deadline nou:","%d %m %Y", "Deadline invalid!")

    if modify_lab(laboratoare, nr_lab, descriere, deadline):
        print("Laborator modificat cu succes!")
    else:
        print("Laboratorul nu a fost modificat!")


def add_menu(studenti, laboratoare):
    cls()
    print_add_menu()
    while True:
        cmd = input("Comanda:")
        match cmd:
            case '1':
                cls()
                add_student_ui(studenti)
                print_all_students(studenti)
                print_add_menu()


            case '2':
                cls()
                modify_student_ui(studenti)
                print_all_students(studenti)
                print_add_menu()
            case '3':
                cls()
                add_lab_ui(laboratoare)
                print_all_labs(laboratoare)
                print_add_menu()
            case '4':
                cls()
                modify_lab_ui(laboratoare)
                print_all_labs(laboratoare)
                print_add_menu()


            case 'q':
                break


def print_delete_menu():
    print("1. Șterge student")
    print("2. Șterge laborator")
    print("q. Back")


def delete_student_ui(studenti):
    """
    Functia sterge studentul cu id-ul dat
    :param studenti:
    :return:
    """
    id = read_number("Id:", int, "Id-ul trebuie sa fie un numar intreg")
    if delete_student(studenti, id):
        print("Student sters cu succes!")
    else:
        print("Studentul nu a fost sters!")


def delete_lab_ui(laboratoare):
    """
    Functia sterge laboratorul cu id-ul dat
    :param laboratoare:
    :return:
    """
    id = read_number("Id:", int, "Id-ul trebuie sa fie un numar intreg")
    if delete_lab(laboratoare, id):
        print("Laborator sters cu succes!")
    else:
        print("Laboratorul nu a fost sters!")


def delete_menu(studenti, laboratoare):
    cls()
    print_delete_menu()
    while True:
        cmd = input("Comanda:")
        match cmd:
            case '1':
                cls()
                delete_student_ui(studenti)
                print_all_students(studenti)
                print_delete_menu()


            case '2':
                cls()
                delete_lab_ui(laboratoare)
                print_all_labs(laboratoare)
                print_delete_menu()
            case 'q':
                break


def main_menu(studenti, laboratoare):
    cls()
    print_main_menu()
    while True:
        cmd = input("Comanda:")

        match cmd:
            case '1':
                add_menu(studenti, laboratoare)
                cls()
                print_main_menu()
            case '2':
                delete_menu(studenti, laboratoare)
                cls()
                print_main_menu()
            case 'a':
                cls()
                print_all_students(studenti)
                print_all_labs(laboratoare)
                print_main_menu()
            case 'q':
                exit(0)