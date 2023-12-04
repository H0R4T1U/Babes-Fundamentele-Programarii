from Tests.domain_test import test_all_domain
from Tests.test_controller import test_controllers
from Tests.validator_test import test_validators


def main_test():
    """
    Functia de legatura a tuturor testelor

    :return:
    """
    # Repositories tests
    #test_all_repositories()
    test_controllers()
    #test_all_utility()
    test_all_domain()
    test_validators()