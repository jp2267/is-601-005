from copy import deepcopy
import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from IcecreamMachine import IceCreamMachine, STAGE
from IcecreamExceptions import InvalidOperation, OutOfStockException, ExceededRemainingChoicesException
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    icm = IceCreamMachine()
    return icm

@pytest.fixture
def first_order(machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("done")
    #machine.handle_pay(2,"2")
    return machine
@pytest.fixture
def second_order(machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("sprinkles")
    machine.handle_toppings("sprinkles")
    machine.handle_toppings("sprinkles")
    machine.handle_toppings("done")
    machine.handle_pay(2.75,"2.75")
    return machine

# Ucid: jp2267 - 22-oct-2022
@pytest.fixture
def third_order(second_order):
    second_order.handle_container("cup")
    second_order.handle_flavor("vanilla")
    second_order.handle_flavor("next")
    second_order.handle_toppings("sprinkles")
    second_order.handle_toppings("sprinkles")
    second_order.handle_toppings("sprinkles")
    second_order.handle_toppings("done")
    second_order.handle_pay(2.75,"2.75")
    return second_order

'''def test_production_line(second_order):
    assert second_order is not None'''

# Ucid: jp2267 
# 1st test case - 22-oct-2022
def test_first_container():
    machine = IceCreamMachine()
    with pytest.raises(InvalidOperation):
        assert machine.currently_selecting == STAGE.Container
        machine.handle_flavor("vanilla")

# Ucid: jp2267 
# 2nd test case - 22-oct-2022
def test_add_flavors_in_stock():
    machine = IceCreamMachine()
    machine.flavors[0].quantity=0
    with pytest.raises(OutOfStockException):
        machine.handle_container("cup")
        machine.handle_flavor("vanilla")

# Ucid: jp2267 
# 3rd test case - 22-oct-2022
def test_add_toppings_in_stock():
    machine = IceCreamMachine()
    machine.toppings[0].quantity=0
    with pytest.raises(OutOfStockException):
        machine.handle_container("cup")
        machine.handle_flavor("vanilla")
        machine.handle_flavor("next")
        machine.handle_toppings("sprinkles")

# Ucid: jp2267 
# 4th test case - 22-oct-2022
def test_max_scoops():
    machine = IceCreamMachine()
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_container("cup")
        machine.handle_flavor("vanilla")
        machine.handle_flavor("vanilla")
        machine.handle_flavor("vanilla")
        machine.handle_flavor("vanilla")

# Ucid: jp2267 
# 5th test case - 22-oct-2022
def test_max_toppings():
    machine = IceCreamMachine()
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_container("cup")
        machine.handle_flavor("vanilla")
        machine.handle_flavor("next")
        machine.handle_toppings("sprinkles")
        machine.handle_toppings("sprinkles")
        machine.handle_toppings("sprinkles")
        machine.handle_toppings("sprinkles")

# Ucid: jp2267 
# 6th test case - 22-oct-2022
def test_cost_calculation(first_order):
    final_cost = 0
    final_cost = first_order.calculate_cost()
    assert final_cost == 2

# Ucid: jp2267 - 22-oct-2022
#7th test case
def test_total_sales(third_order):
    total_sales = 0
    total_sales = third_order.total_sales
    assert total_sales == 5.5

# Ucid: jp2267 - 22-oct-2022
#8th test case
def test_total_icreams(third_order):
    total_icecreams = 0
    total_icecreams = third_order.total_icecreams
    assert total_icecreams == 2