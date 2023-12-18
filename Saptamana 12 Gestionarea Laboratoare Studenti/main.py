from Repository.LabRepository import LabRepository
from Repository.StudentiRepository import StudentRepository

from UI.main_menu import main_menu

if __name__ == '__main__':
    studenti = StudentRepository("Data/studenti.txt")
    studenti.load()
    laboratoare = LabRepository("Data/lab.txt")
    laboratoare.load()
    main_menu(studenti, laboratoare)
