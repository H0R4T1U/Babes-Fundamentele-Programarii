from Tests.test_assign_controller import test_assign_controller
from Tests.test_crud_controller import test_crud_controller
from Tests.test_functionalitati_controller import test_func_controller

def test_controllers():
    test_crud_controller()
    test_assign_controller()
    test_func_controller()
