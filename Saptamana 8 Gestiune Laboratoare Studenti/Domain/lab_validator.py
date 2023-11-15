import datetime




def validate_lab(laborator, laboratoare):
    msg = ""

    if laborator.id in [lab.id for lab in laboratoare]:
        msg += "Laboratorul exista deja!\n"
    if laborator.id < 0:
        msg += "Numarul laboratorului nu poate fi negativ!\n"
    if laborator.descriere == "":
        msg += "Descrierea nu poate fi vida!\n"
    if laborator.deadline.year < 2023 or laborator.deadline.year > 2024:
        msg += "Deadline Invalid\n"
    if msg != "":
        raise ValueError(msg)
    else:
        return True
