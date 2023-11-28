from Controller.asign_controller import assign_lab, assign_nota
from Controller.crud import add_student, modify_student, delete_student, add_lab, modify_lab, delete_lab
from Controller.functionalitati_controller import cauta_student, cauta_laborator, stat_stud_lab, stat_stud_medie_5, \
    stat_stud_lab_10
from Repository.file_repository import create_x_labs, create_x_students
from Utility.utility import read_number, cls, read_date
from Views.app_view import print_all_students, print_all_labs, afiseaza_note_studenti, afiseaza_stud_corigenti


def print_main_menu():
    print("1. Meniu Adăugări/Modificări")
    print("2. Meniu Ștergeri")
    print("3. Meniu Căutări")
    print("4. Meniu Statistici")
    print("X. Crează X studenti și laboratoare")
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


def print_delete_menu():
    print("1. Șterge student")
    print("2. Șterge laborator")
    print("q. Back")


def print_cautare_menu():
    print("1. Caută student")
    print("2. Caută Laborator")
    print("q. Back")


def print_statistici_menu():
    print("1. Note studenti laborator")
    print("2. Studenti Corigenti")
    print("3. Note Studenti Laborator 10%")
    print("q. Back")


def add_student_ui(studenti):
    nume = input("Nume:")
    grupa = read_number("Grupa:", int, "Grupa trebuie sa fie un numar intreg")
    try:
        add_student(studenti, nume, grupa)
    except ValueError as ve:
        print(ve)
    else:
        print("Student adăugat cu succes!")


def modify_student_ui(studenti):
    id = read_number("Id:", int, "Id-ul trebuie sa fie un numar intreg")
    nume = input("Nume nou:")
    grupa = read_number("Grupa noua:", int, "Grupa trebuie sa fie un numar intreg")

    try:
        modify_student(studenti, id, nume, grupa)
    except ValueError as ve:
        print(ve)
    except Exception as ex:
        print(ex)
    else:
        print("Student Modificat cu succes!")


def add_lab_ui(laboratoare):
    nr_lab = read_number("Numar laborator:", int, "Numarul laboratorului trebuie sa fie un numar intreg")
    descriere = input("Descriere:")
    deadline = read_date("Deadline(zi luna an):", "%d %m %Y", "Deadline invalid!")
    try:
        add_lab(laboratoare, nr_lab, descriere, deadline)
    except ValueError as ve:
        print(ve)
    else:
        print("Laborator adăugat cu succes!")


def modify_lab_ui(laboratoare):
    nr_lab = read_number("Numar laborator:", int, "Numarul laboratorului trebuie sa fie un numar intreg")
    descriere = input("Descriere noua:")
    deadline = read_date("Deadline nou(zi luna an):", "%d %m %Y", "Deadline invalid!")

    try:
        modify_lab(laboratoare, nr_lab, descriere, deadline)
    except ValueError as ve:
        print(ve)
    except Exception as ex:
        print(ex)
    else:
        print("Laborator modificat cu succes!")


def assign_stud_lab_ui(studenti, laboratoare):
    id = None
    nume = None
    print("1. Caută după nume")
    print("2. Caută dupa ID")
    while True:
        cmd = input(':').lower()
        match cmd:
            case '1':
                nume = input("Nume Student:")
                break
            case '2':
                id = read_number("Id Student:", int, "Id student trebuie să fie >0")
                break
            case _:
                print("Comandă Invalidă!")
    lab = read_number("Nr Laborator:", int, "Nr laborator trebuie să fie > 0")
    try:
        assign_lab(studenti, laboratoare, lab, nume, id)
    except Exception as ex:
        print(ex)
    else:
        print("Laborator asignat cu succes!")


def assign_nota_lab_ui(studenti, laboratoare):
    id = None
    nume = None
    print("1. Caută după nume")
    print("2. Caută dupa ID")
    while True:
        cmd = input(':').lower()
        match cmd:
            case '1':
                nume = input("Nume Student:")
                break
            case '2':
                id = read_number("Id Student:", int, "Id student trebuie să fie nr întreg")
                break
            case _:
                print("Comandă Invalidă!")
    lab = read_number("Nr Laborator:", int, "Nr laborator trebuie să fie nr întreg")
    nota = read_number("Nota obținută:", int, "Nota trebuie să fie număr întreg")
    try:
        assign_nota(studenti, laboratoare, lab, nota, nume, id)
    except Exception as ex:
        print(ex)
    else:
        print("Laborator asignat cu succes!")


def add_menu(studenti, laboratoare):
    cls()
    print_add_menu()
    while True:
        cmd = input("Comanda:").lower()
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
            case '5':
                cls()
                assign_stud_lab_ui(studenti, laboratoare)
                print_add_menu()
            case '6':
                cls()
                assign_nota_lab_ui(studenti, laboratoare)
                print_add_menu()
            case 'q':
                break
            case _:
                print("comanda invalida!")


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
        cmd = input("Comanda:").lower()
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
            case _:
                print("comanda invalida!")


def cautare_student_ui(studenti):
    id = None
    nume = None
    print("1. Caută după Nume")
    print("2. Caută dupa ID")
    while True:
        cmd = input('Comanda:').lower()
        match cmd:
            case '1':
                nume = input("Nume Student:")
                break
            case '2':
                id = read_number("Id Student:", int, "Id student trebuie să fie nr întreg")
                break
            case _:
                print("Comandă Invalidă!")
    try:
        print_all_students([cauta_student(studenti, nume, id)])
    except Exception as ex:
        print(ex)


def cautare_laborator_ui(laboratoare):
    id = read_number("Id Laborator:", int, "Id laborator trebuie să fie nr întreg")
    try:
        print_all_labs([cauta_laborator(laboratoare, id)])
    except Exception as ex:
        print(ex)


def cautare_menu(studenti, laboratoare):
    print_cautare_menu()
    while True:
        cmd = input("Comanda:").lower()
        match cmd:
            case '1':
                cls()
                cautare_student_ui(studenti)
                print_cautare_menu()

            case '2':
                cls()
                cautare_laborator_ui(laboratoare)
                print_cautare_menu()
            case 'q':
                break
            case _:
                print("comanda invalida!")


def stat_stud_lab_ui(studenti):
    id = read_number("Nr lab:", int, 'id-ul laboratorului trebuie sa fie întreg')
    try:
        studenti = stat_stud_lab(studenti, id)
        afiseaza_note_studenti(studenti,id)
    except Exception as ex:
        print(ex)


def stat_stud_medie_5_ui(studenti):
    try:
        studenti = stat_stud_medie_5(studenti)
        afiseaza_stud_corigenti(studenti)
    except Exception as ex:
        print(ex)


def stat_stud_lab_10_ui(studenti):
    id = read_number("Nr lab:", int, 'id-ul laboratorului trebuie sa fie întreg')
    try:
        studenti = stat_stud_lab_10(studenti, id)
        afiseaza_note_studenti(studenti, id)
    except Exception as ex:
        print(ex)


def statistici_menu(studenti):
    print_statistici_menu()
    while True:
        cmd = input("Comanda:").lower()
        match cmd:
            case '1':
                cls()
                stat_stud_lab_ui(studenti)
                print_statistici_menu()
            case '2':
                cls()
                stat_stud_medie_5_ui(studenti)
                print_statistici_menu()
            case '3':
                cls()
                stat_stud_lab_10_ui(studenti)
                print_statistici_menu()
            case 'q':
                break
            case _:
                print("Comanda invalidă!")


def create_x_students_ui(studenti, laboratoare):

    nr_lab = read_number("Nr laboratoare:",int,"Nr de laboratore trebuie sa fie nr intreg!")
    while nr_lab <= 0:
        print("Nr de laboratoare trebuie sa fie un numar pozitiv mai mare ca 0!")
        nr_lab = read_number("Nr laboratoare:", int, "Nr de laboratore trebuie sa fie nr intreg!")

    nr_stud = read_number("Nr studenti:",int,'Nr de studenti trebuie sa fie nr intreg!')
    while nr_stud <= 0:
        print("Nr de studenti trebuie sa fie un numar pozitiv mai mare ca 0!")
        nr_stud = read_number("Nr studenti:", int, 'Nr de studenti trebuie sa fie nr intreg!')
    create_x_labs(nr_lab,laboratoare)
    create_x_students(nr_stud,studenti,laboratoare)


def main_menu(studenti, laboratoare):
    cls()
    print_main_menu()
    while True:
        cmd = input("Comanda:").lower()

        match cmd:
            case '1':
                add_menu(studenti, laboratoare)
                cls()
                print_main_menu()
            case '2':
                delete_menu(studenti, laboratoare)
                cls()
                print_main_menu()
            case '3':
                cautare_menu(studenti, laboratoare)
                cls()
                print_main_menu()
            case '4':
                statistici_menu(studenti)
                cls()
                print_main_menu()
            case 'a':
                cls()
                print_all_students(studenti)
                print_all_labs(laboratoare)
                print_main_menu()
            case 'x':
                cls()
                create_x_students_ui(studenti,laboratoare)
                print_main_menu()
            case 'q':
                exit(0)
            case _:
                print("comanda invalida!")
