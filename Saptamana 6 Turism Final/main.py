from UI.console import main_menu
from Tests.main_tests import main_test


def run():
    pachete = []
    undo_list = []
    main_test()
    main_menu(pachete, undo_list)


run()
