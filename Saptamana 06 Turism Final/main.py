from Batch.batchmode import batch_mode
from UI.console import main_menu
from Tests.main_tests import main_test


def run():
    pachete = []
    undo_list = []

    flag = True
    while flag:
        print("1. Normal Mode")
        print("2. Batch Mode")
        cmd = input(":")
        match cmd:
            case "1":
                main_test()
                main_menu(pachete, undo_list)
                flag = True
            case "2":
                batch_mode(pachete, undo_list)
                flag = False



run()
