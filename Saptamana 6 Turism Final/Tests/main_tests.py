from Tests.repository_tests import test_all_repositories
from Tests.Service_tests import test_all_services
from Tests.utility_test import test_all_utility


def main_test():
    """
    Functia de legatura a tuturor testelor
    :param a: lista cu elementele de testat
    :return:
    """
    # Repositories tests
    test_all_repositories()
    test_all_services()
    test_all_utility()
