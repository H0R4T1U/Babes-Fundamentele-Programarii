import datetime

from Domain.Laborator import get_nr_lab, get_deadline, get_descriere


def validate_lab(laborator, laboratoare):
    msg = ""

    if get_nr_lab(laborator) in [get_nr_lab(lab) for lab in laboratoare]:
        msg += "Laboratorul exista deja!\n"
    if get_nr_lab(laborator) < 0:
        msg += "Numarul laboratorului nu poate fi negativ!\n"
    if get_descriere(laborator) == "":
        msg += "Descrierea nu poate fi vida!\n"
    if get_deadline(laborator).year < 2023 or get_deadline(laborator).year > 2024:
        msg += "Deadline Invalid\n"
    if msg != "":
        raise ValueError(msg)
    else:
        return True
