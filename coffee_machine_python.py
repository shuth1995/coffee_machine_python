# Coffee Machine Simulator
# This program simulates a coffee vending machine that can sell drinks,
# refill ingredients, display resources, and handle cash withdrawals.

# --- Coffee class to represent a drink order ---
class Coffee:
    def __init__(self, cups):
        self.cups = cups
        self.water_per_cup = 0
        self.milk_per_cup = 0
        self.beans_per_cup = 0
        self.cost_per_cup = 0

    # Espresso configuration: 250 ml water, 0 ml milk, 16 g beans, $4
    @staticmethod
    def espresso(cups):
        coffee = Coffee(cups)
        coffee.water_per_cup = 250
        coffee.milk_per_cup = 0
        coffee.beans_per_cup = 16
        coffee.cost_per_cup = 4
        return coffee

    # Latte configuration: 350 ml water, 75 ml milk, 20 g beans, $7
    @staticmethod
    def latte(cups):
        coffee = Coffee(cups)
        coffee.water_per_cup = 350
        coffee.milk_per_cup = 75
        coffee.beans_per_cup = 20
        coffee.cost_per_cup = 7
        return coffee

    # Cappuccino configuration: 200 ml water, 100 ml milk, 12 g beans, $6
    @staticmethod
    def cappuccino(cups):
        coffee = Coffee(cups)
        coffee.water_per_cup = 200
        coffee.milk_per_cup = 100
        coffee.beans_per_cup = 12
        coffee.cost_per_cup = 6
        return coffee

    # Calculate total ingredients needed for the specified number of cups
    def calculate_ingredients(self):
        return (
            self.water_per_cup * self.cups,
            self.milk_per_cup * self.cups,
            self.beans_per_cup * self.cups
        )

# --- Coffee Machine class to manage inventory and cash ---
class Coffee_machine:
    def __init__(self):
        self.cash = 550
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9

# Create a Coffee_machine instance to track machine state
machine = Coffee_machine()

# --- Function to display current machine resources ---
def display_availability(machine):
    print(f"The coffee machine has:\n"
          f"{machine.water} ml of water\n"
          f"{machine.milk} ml of milk\n"
          f"{machine.beans} g of coffee beans\n"
          f"{machine.cups} disposable cups\n"
          f"${machine.cash} of money\n")

# --- Function to process a drink purchase and deduct ingredients ---
def process_purchase(order, machine):
    required_water, required_milk, required_beans = order.calculate_ingredients()

    if machine.water >= required_water and machine.milk >= required_milk and machine.beans >= required_beans and machine.cups >= order.cups:
        machine.water -= required_water
        machine.milk -= required_milk
        machine.beans -= required_beans
        machine.cups -= order.cups
        machine.cash += order.cost_per_cup * order.cups
        print("I have enough resources, making you a coffee!")
    elif machine.water < required_water:
        print("Sorry, not enough water!")
    elif machine.milk < required_milk:
        print("Sorry, not enough milk!")
    elif machine.beans < required_beans:
        print("Sorry, not enough coffee beans!")
    elif machine.cups == 0:
        print("Sorry, not enough cups!")
    else:
        print("Sorry, not enough ingredients to make that coffee.")

# --- Function to refill machine resources from user input ---
def fill_machine(machine):
    add_water = int(input("Write how many ml of water you want to add:\n"))
    add_milk = int(input("Write how many ml of milk you want to add:\n"))
    add_beans = int(input("Write how many grams of beans you want to add:\n"))
    add_cups = int(input("Write how many disposable cups you want to add:\n"))

    machine.water += add_water
    machine.milk += add_milk
    machine.beans += add_beans
    machine.cups += add_cups

# --- Function to withdraw all money from the machine ---
def withdraw_money(machine):
    print(f"I gave you ${machine.cash}")
    machine.cash = 0

# --- Main interaction loop ---
while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")

    if action == "buy":
        # Prompt user for drink selection
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if coffee_type == "back":
            continue
        coffee_type = int(coffee_type)
        if coffee_type == 1:
            order = Coffee.espresso(1)
        elif coffee_type == 2:
            order = Coffee.latte(1)
        elif coffee_type == 3:
            order = Coffee.cappuccino(1)
        print("")
        process_purchase(order, machine)

    elif action == "fill":
        print("")
        fill_machine(machine)

    elif action == "take":
        print("")
        withdraw_money(machine)

    elif action == "remaining":
        print("")
        display_availability(machine)

    elif action == "exit":
        break
