import os

def cls():
    os.system('clear' if os.name == 'posix' else 'cls')


def citire_nr(prompt, f, msg):
    """
    Citeste un nr si il returneaza ca si int
    :param prompt: Ce se afiseaza
    :param f: functia de convertire
    :param msg: error msg
    :return:
    """
    while True:
        try:
            return f(input(prompt))
        except ValueError:
            print(msg)
