def creaza_student(id, nume, grupa):
    return {'id': id, 'nume': nume, 'grupa': grupa, 'laboratoare': [], 'note': [] }


def get_id(student):
    return student['id']


def get_nume(student):
    return student['nume']


def get_grupa(student):
    return student['grupa']


def get_laboratoare(student):
    return student['laboratoare']


def get_note(student):
    return student['note']

# setters for all parmas
def set_id(student, id):
    student['id'] = id


def set_nume(student, nume):
    student['nume'] = nume


def set_grupa(student, grupa):
    student['grupa'] = grupa


def set_laboratoare(student, laboratoare):
    student['laboratoare'] = laboratoare


def set_note(student, note):
    student['note'] = note



