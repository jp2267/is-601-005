from enum import Enum
import time
# make a tests folder under the folder you're putting these files in
# add an empty __init__.py to the tests folder
from IcecreamExceptions import ExceededRemainingChoicesException, InvalidChoiceException, NeedsCleaningException, OutOfStockException
from IcecreamExceptions import InvalidPaymentException, InvalidOperation

class Usable:
    name = ""
    quantity = 0
    cost = 99

    def __init__(self, name, quantity = 10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def use(self):
        self.quantity -= 1
        if (self.quantity < 0):
            raise OutOfStockException
        return self.quantity 

    def in_stock(self):
        return self.quantity > 0

class Container(Usable):
    pass

class Flavor(Usable):
    pass

class Toppings(Usable):
    pass

class STAGE(Enum):
    Container = 1
    Flavor = 2
    Toppings = 3
    Pay = 4

class IceCreamMachine:
    # Constants https://realpython.com/python-constants/
    USES_UNTIL_CLEANING = 100
    MAX_SCOOPS = 3
    MAX_TOPPINGS = 3

    def __init__(self):
        self.containers = [Container(name="Waffle Cone", cost=1.5), Container(name="Sugar Cone", cost=1), Container("Cup", cost=1)]
        self.flavors = [Flavor(name="Vanilla", quantity=100, cost=1), Flavor(name="Chocolate", quantity=100, cost=1), Flavor(name="Strawberry", quantity=100, cost=1)]
        self.toppings = [Toppings(name="Sprinkles", quantity=200, cost=.25), Toppings(name="Chocolate Chips", quantity=200, cost=.25), Toppings(name="M&Ms", quantity=200, cost=.25), \
            Toppings(name="Gummy Bears", quantity=200, cost=.25), Toppings(name="Peanuts", quantity=200, cost=.25)] 
        self.inprogress_icecream = []

    # variables
    remaining_uses = USES_UNTIL_CLEANING
    remaining_scoops = MAX_SCOOPS
    remaining_toppings = MAX_TOPPINGS
    total_sales = 0
    total_icecreams = 0

    currently_selecting = STAGE.Container

    # rules
    # 1 - container must be chosen first
    # 2 - can only use items if there's quantity remaining
    # 3 - scoops can't exceed max
    # 4 - toppings can't exceed max
    # 5 - a container and at least 1 scoop or toppings must be selected
    # 6 - proper cost must be calculated and shown to the user
    # 7 - cleaning must be done after certain number of uses before any more icecreams can be made
    # 8 - total sales should calculate properly based on cost calculation
    # 9 - total_icecreams should increment properly after a payment
    

    def pick_container(self, choice):
        for c in self.containers:
            if c.name.lower() == choice:
                c.use()
                self.inprogress_icecream.append(c)
                return
        raise InvalidChoiceException

    def pick_flavor(self, choice):
        if self.remaining_uses <= 0:
            raise NeedsCleaningException
        if self.remaining_scoops <= 0:
            raise ExceededRemainingChoicesException
        for f in self.flavors:
            if f.name.lower() == choice:
                f.use()
                self.inprogress_icecream.append(f)
                self.remaining_scoops -= 1
                self.remaining_uses -= 1
                return
        raise InvalidChoiceException

    def pick_toppings(self, choice):
        if self.remaining_toppings <= 0:
            raise ExceededRemainingChoicesException
        for t in self.toppings:
            if t.name.lower() == choice:
                t.use()
                self.inprogress_icecream.append(t)
                self.remaining_toppings -= 1
                return
        raise InvalidChoiceException

    def reset(self):
        self.remaining_scoops = self.MAX_SCOOPS
        self.remaining_toppings = self.MAX_TOPPINGS
        self.inprogress_icecream = []
        self.currently_selecting = STAGE.Container

    def clean_machine(self):
        self.remaining_uses = self.USES_UNTIL_CLEANING
        
    def handle_container(self, container):
        if self.currently_selecting != STAGE.Container:
            raise InvalidOperation
        self.pick_container(container)
        self.currently_selecting = STAGE.Flavor

    def handle_flavor(self, flavor):
        if self.currently_selecting != STAGE.Flavor:
            raise InvalidOperation
        if flavor == "next":
            self.currently_selecting = STAGE.Toppings
        else:
            self.pick_flavor(flavor)

    def handle_toppings(self, toppings):
        if self.currently_selecting != STAGE.Toppings:
            raise InvalidOperation
        if toppings == "done":
            self.currently_selecting = STAGE.Pay
        else:
            self.pick_toppings(toppings)

    def handle_pay(self, expected, total):
        if total == str(expected):
            print("Thank you! Enjoy your icecream!")
            self.total_icecreams += 1
            self.total_sales += expected # only if successful
            print("total sales: ",self.total_sales)
            print("Remaining Uses: ",self.remaining_uses)
            self.reset()
        else:
            raise InvalidPaymentException
    
    # Ucid: jp2267 - 22-oct-2022
    # Calculate method which calculates the total cost of the icecream       
    def calculate_cost(self):
        # TODO add the calculation expression/logic for the inprogress_icecream
        return sum(self.inprogress_icecream[i].cost for i in range(len(self.inprogress_icecream)))

    def run(self):
        if self.currently_selecting == STAGE.Container:
            try:
                container = input(f"Would you like a {', '.join(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.containers))))}?\n")
                self.handle_container(container)
            
            # Ucid: jp2267 - 22-oct-2022
            # Invalid choice exception is handled
            except InvalidChoiceException:
                print(f"Invalid choice please enter a valid choice \n such as a {', '.join(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.containers))))}?\n")
            
            # Ucid: jp2267 - 22-oct-2022
            # out of stock exception is handled
            except OutOfStockException:
                print("Sorry the machine is out of stock for the container which you need please enter a container from the below available containers")

        elif self.currently_selecting == STAGE.Flavor:
            try:
                flavor = input(f"Would you like {', '.join(list(map(lambda f:f.name.lower(), filter(lambda f: f.in_stock(), self.flavors))))}? Or type next.\n")
                self.handle_flavor(flavor)
            
            # Ucid: jp2267 - 22-oct-2022
            # Invalid choice exception is handled
            except InvalidChoiceException:
                print(f"Invalid choice please enter a valid choice \n such as a {', '.join(list(map(lambda f:f.name.lower(), filter(lambda f: f.in_stock(), self.flavors))))}? Or type next.\n")
            
            # Ucid: jp2267 - 22-oct-2022
            # Exceeded Remaining Choices Exception is handled
            except ExceededRemainingChoicesException:
                print("Sorry you have your max scoops (which is 3) \n please type next to add the toppings in your icecream")
            
            # Ucid: jp2267 - 22-oct-2022
            # Out of Stock Exception is handled
            except OutOfStockException:
                print("Sorry the machine is out of stock for the flavor which you need please enter a flavor from the below available flavors")
            
            # Ucid: jp2267 - 22-oct-2022
            # Needs Cleaning Exception is handled
            except NeedsCleaningException:
                self.remaining_uses = self.USES_UNTIL_CLEANING
                print("Sorry the machine is under cleaning stage please wait for 5 seconds")
                time.sleep(5)
                print("The machine is now ready to use")

        elif self.currently_selecting == STAGE.Toppings:
            try:
                toppings = input(f"Would you like {', '.join(list(map(lambda t:t.name.lower(), filter(lambda t: t.in_stock(), self.toppings))))}? Or type done.\n")
                self.handle_toppings(toppings)
            
            # Ucid: jp2267 - 22-oct-2022
            # Invalid Choice Exception is handled
            except InvalidChoiceException:
                print(f"Invalid choice please enter a valid choice \n such as a {', '.join(list(map(lambda t:t.name.lower(), filter(lambda t: t.in_stock(), self.toppings))))}? Or type done.\n")
            
            # Ucid: jp2267 - 22-oct-2022
            # Exceeded Remaining Choices Exception is handled
            except ExceededRemainingChoicesException:
                print("Sorry you have your max toppings (which is 3) \n please type done to get your")

            # Ucid: jp2267 - 22-oct-2022
            # Out of Stock Exception is handled
            except OutOfStockException:
                print("Sorry the machine is out of stock for the flavor which you need please enter a flavor from the below available flavors")

            # Ucid: jp2267 - 22-oct-2022
            # Needs Cleaning Exception is handled
            except NeedsCleaningException:
                self.remaining_uses = self.USES_UNTIL_CLEANING
                print("Sorry the machine is under cleaning stage please wait for 5 seconds")
                time.sleep(5)
                print("The machine is now ready to use")

        elif self.currently_selecting == STAGE.Pay:
            expected = self.calculate_cost()
            try:
                total = input(f"Your total is {expected}, please enter the exact value.\n")
                self.handle_pay(expected, total)
                choice = input("What would you like to do? (icecream or quit)\n")
                if choice == "quit":
                    exit()

            # Ucid: jp2267 - 22-oct-2022
            # Invalid Payment Exception Handled
            except InvalidPaymentException:
                print("Transaction failed")

        self.run()

    def start(self):
        self.run()

    
if __name__ == "__main__":
    icm = IceCreamMachine()
    icm.start()