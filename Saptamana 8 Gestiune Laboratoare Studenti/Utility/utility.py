from datetime import datetime
import os

def cls():
    """
    Clears the screen
    :return:
    """

    os.system('clear' if os.name == 'posix' else 'cls')

def read_number(prompt, func, msg):
    while True:
        try:
            return func(input(prompt))
        except ValueError:
            print(msg)


def read_date(prompt, format, msg):

    while True:

        try:
            return datetime.strptime(input(f"{prompt}"), format)
        except ValueError:
            print(msg)
